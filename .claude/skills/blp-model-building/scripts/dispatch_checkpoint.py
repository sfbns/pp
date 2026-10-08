#!/usr/bin/env python3
"""Execute one bound checkpoint action without interpreting its payload files.

The output directory must be new. A launch is subprocess.Popen(shell=False), not
a proposed command. This is a project controller, not native-agent registration.
"""
from __future__ import annotations

import argparse
import base64
import copy
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

REQUIRED_FIELDS = (
    "ACTIVE_OBJECT", "LAST_CONFIRMED_RESULT", "NEXT_EXECUTABLE_ACTION",
    "INPUT_PATHS", "ACCEPTANCE_EVENT",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def absolute(path: str | os.PathLike[str]) -> Path:
    # abspath does not open a Windows file handle; physical aliases are checked
    # separately where paths exist. Never rewrite the child command or cwd.
    return Path(os.path.abspath(os.fspath(path)))


def contained(path: Path, parent: Path) -> bool:
    try:
        return os.path.commonpath((str(path), str(parent))) == str(parent)
    except ValueError:
        return False


def physical(path: Path) -> Path:
    return Path(os.path.realpath(str(path)))


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def validate_command(action: object) -> tuple[list[str], str]:
    if not isinstance(action, dict):
        raise TypeError("NEXT_EXECUTABLE_ACTION must be a JSON object")
    if action.get("completed") is True or action.get("status") in {"complete", "completed", "success"}:
        raise ValueError("The bound action is already completed; refusing to rerun it")
    command = action.get("command_array")
    if not isinstance(command, list) or not command:
        raise TypeError("command_array must be a nonempty JSON array of strings")
    if any(not isinstance(arg, str) or "\x00" in arg for arg in command) or not command[0]:
        raise TypeError("command_array elements must be strings without NUL; executable must be nonempty")
    cwd = action.get("cwd")
    if not isinstance(cwd, str) or not cwd or "\x00" in cwd:
        raise TypeError("cwd must be a nonempty string without NUL")
    # No normalization or argument substitution: relative inputs are interpreted
    # by the child from this exact cwd.
    return copy.deepcopy(command), cwd


def select_template(checkpoint: dict, bound: dict, original: dict) -> tuple[dict, dict]:
    """An explicitly named, successful, identity-matched template is optional."""
    metadata_path = checkpoint.get("controller_command_metadata_path")
    selection = {"source": "NEXT_EXECUTABLE_ACTION", "metadata_path": metadata_path,
                 "template_applied": False}
    if metadata_path is None:
        return original, selection
    try:
        if not isinstance(metadata_path, str) or not metadata_path:
            raise TypeError("controller_command_metadata_path must be a nonempty string")
        identity = checkpoint.get("identity")
        if not isinstance(identity, dict) or not identity:
            raise ValueError("A nonempty checkpoint identity is required to match a controller template")
        # This is the only optional project file read by the dispatcher. Input
        # paths, prompts, reports, tests and other payloads are not opened here.
        raw = Path(metadata_path).read_bytes()
        metadata = json.loads(raw)
        if not isinstance(metadata, dict):
            raise TypeError("Controller command metadata must be an object")
        success = metadata.get("success") is True or metadata.get("status") == "success"
        if not success or metadata.get("identity") != identity:
            raise ValueError("Controller template is not successful and identity-matched")
        candidate = {"command_array": metadata.get("command_array"), "cwd": metadata.get("cwd")}
        validate_command(candidate)
        selection.update(source="controller_command_metadata_path", template_applied=True,
                         metadata_sha256=sha256(raw), matched_identity=copy.deepcopy(identity))
        return candidate, selection
    except Exception as exc:
        selection["fallback_reason"] = f"{type(exc).__name__}: {exc}"
        return original, selection


def run(checkpoint_arg: str, out_arg: str) -> int:
    checkpoint_path = absolute(checkpoint_arg)
    out = absolute(out_arg)
    # Refusal never touches an existing evidence directory, including symlinks.
    if os.path.lexists(out):
        print(json.dumps({"error": "OutputExistsError", "message": "--out must not exist",
                          "out": str(out), "started": False}), file=sys.stderr)
        return 73

    event = {"schema_version": 1, "role": "project_checkpoint_dispatcher",
             "native_agent_registration": False, "utc_started": utc(),
             "checkpoint_path": str(checkpoint_path), "out": str(out),
             "started": False, "pid": None, "shell": False,
             "actual_command_array": None, "actual_cwd": None,
             "literal_stdout": "", "literal_stderr": "", "exit_status": None}
    before = None
    bound = None
    created = False
    return_code = 64
    try:
        before = checkpoint_path.read_bytes()
        event["checkpoint_sha256_before"] = sha256(before)
        checkpoint = json.loads(before)
        if not isinstance(checkpoint, dict):
            raise TypeError("Checkpoint must be a JSON object")
        missing = [name for name in REQUIRED_FIELDS if name not in checkpoint]
        if missing:
            raise KeyError("Missing required checkpoint fields: " + ", ".join(missing))
        # This binding is write-once. No subsequent project discovery changes it.
        bound = {name: copy.deepcopy(checkpoint[name]) for name in REQUIRED_FIELDS}
        binding_json = json.dumps(bound, sort_keys=True, ensure_ascii=True)
        event["bound_fields"] = copy.deepcopy(bound)
        event["binding_sha256"] = sha256(binding_json.encode("utf-8"))
        active_object = bound["ACTIVE_OBJECT"]
        if not isinstance(active_object, str) or not active_object:
            raise TypeError("ACTIVE_OBJECT must be a nonempty path string")
        target = physical(absolute(active_object))
        physical_out = physical(out)
        if physical_out == physical(checkpoint_path):
            raise ValueError("Output must not replace the checkpoint")
        # A candidate may be either a file or a directory. A directory's whole
        # tree is immutable controller input; a file itself may not be replaced.
        if physical_out == target or (target.is_dir() and contained(physical_out, target)):
            raise ValueError("Output must be outside ACTIVE_OBJECT/candidate")
        out.mkdir(parents=True, exist_ok=False)
        created = True
        original_action = bound["NEXT_EXECUTABLE_ACTION"]
        event["original_action"] = copy.deepcopy(original_action)
        # Validate the pending original even when optional metadata is present.
        validate_command(original_action)
        selected, selection = select_template(checkpoint, bound, original_action)
        command, cwd = validate_command(selected)
        event["command_selection"] = selection
        event["actual_command_array"] = copy.deepcopy(command)
        event["actual_cwd"] = cwd
        event["pythonutf8_inherited"] = os.environ.get("PYTHONUTF8")
        # No payload read or baseline invocation occurs before this launch.
        process = subprocess.Popen(command, cwd=cwd, shell=False,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        event.update(started=True, pid=process.pid, process_started_utc=utc())
        dump(out / "command_execution.json", event)
        stdout, stderr = process.communicate()
        (out / "stdout.bin").write_bytes(stdout)
        (out / "stderr.bin").write_bytes(stderr)
        # UTF-8 strings are literal where valid. Base64 and .bin retain every
        # original byte even for non-UTF-8 child streams.
        event.update(literal_stdout=stdout.decode("utf-8", errors="surrogateescape"),
                     literal_stderr=stderr.decode("utf-8", errors="surrogateescape"),
                     stdout_base64=base64.b64encode(stdout).decode("ascii"),
                     stderr_base64=base64.b64encode(stderr).decode("ascii"),
                     exit_status=process.returncode, process_finished_utc=utc())
        return_code = process.returncode
    except Exception as exc:
        event["controller_error"] = {"type": type(exc).__name__, "message": str(exc),
                                     "traceback": traceback.format_exc()}
        return_code = 64
    finally:
        if before is not None:
            try:
                after = checkpoint_path.read_bytes()
                event["checkpoint_sha256_after"] = sha256(after)
                event["checkpoint_unchanged"] = after == before
                assert after == before, "Checkpoint bytes changed during dispatched action"
            except Exception as exc:
                event["checkpoint_integrity_error"] = {"type": type(exc).__name__, "message": str(exc)}
                event["checkpoint_unchanged"] = False
                return_code = 74
        if bound is not None:
            assert event["binding_sha256"] == sha256(
                json.dumps(bound, sort_keys=True, ensure_ascii=True).encode("utf-8"))
        event["dispatcher_exit_status"] = return_code
        event["utc_finished"] = utc()
        if created:
            # Native JSON and byte streams are supplementary controller evidence,
            # never an academic evaluation or native registration proof.
            dump(out / "command_execution.json", event)
            if not (out / "stdout.bin").exists():
                (out / "stdout.bin").write_bytes(b"")
            if not (out / "stderr.bin").exists():
                (out / "stderr.bin").write_bytes(b"")
        print(json.dumps({"out": str(out), "event_path": str(out / "command_execution.json") if created else None,
                          "started": event["started"], "pid": event["pid"],
                          "exit_status": event["exit_status"], "dispatcher_exit_status": return_code,
                          "checkpoint_unchanged": event.get("checkpoint_unchanged"),
                          "error": event.get("controller_error")}, ensure_ascii=True))
    return return_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--out", required=True, help="A fresh, nonexistent evidence directory outside the candidate")
    args = parser.parse_args()
    return run(args.checkpoint, args.out)


if __name__ == "__main__":
    raise SystemExit(main())
