#!/usr/bin/env python3
"""Pinned, local-explicit-load preflight. This is not role installation or a sandbox.

Both manifest identities must be pinned by the caller. A manifest hash is an
identity check, not a cryptographic signature. Only the enumerated dependency
snapshot is covered; extra knowledge sources need a new registration/freeze.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import platform
import re
import stat
import subprocess
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path


HEX256 = re.compile(r"[0-9a-fA-F]{64}\Z")
RESERVED = re.compile(r"(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?\Z", re.I)
CHECK_SCRIPTS = ("scripts/scaled_rank_checks.py", "scripts/blp_core_checks.py")
RUNTIME_ENVIRONMENT = "skills/blp-project-professor/references/runtime-environment.json"


class GuardError(Exception):
    def __init__(self, message: str, exit_code: int = 2):
        super().__init__(message)
        self.exit_code = exit_code


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise GuardError("argument error: " + message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(data: bytes):
    return hashlib.sha256(data).hexdigest()


def file_hash(path: Path):
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            h.update(block)
            size += len(block)
    return h.hexdigest(), size


def reparse(st):
    return bool(getattr(st, "st_file_attributes", 0) & 0x400)


def ordinary_file(path: Path):
    st = path.lstat()
    if stat.S_ISLNK(st.st_mode) or reparse(st) or not stat.S_ISREG(st.st_mode):
        raise GuardError("not an ordinary, non-reparse file: " + str(path))


def directory(path: Path, label: str):
    st = path.lstat()
    if stat.S_ISLNK(st.st_mode) or reparse(st) or not stat.S_ISDIR(st.st_mode):
        raise GuardError(label + " is not an ordinary, non-reparse directory: " + str(path))
    return path.resolve(strict=True)


def within(path: Path, root: Path):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def pairs_without_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise GuardError("duplicate JSON key: " + repr(key))
        result[key] = value
    return result


def relative_name(value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise GuardError("manifest path must be a nonempty forward-slash relative string: " + repr(value))
    parts = value.split("/")
    for part in parts:
        if part in ("", ".", "..") or part[-1:] in (".", " "):
            raise GuardError("unsafe relative manifest path: " + repr(value))
        if any(ord(c) < 32 or c in ':<>"|?*' for c in part) or RESERVED.fullmatch(part):
            raise GuardError("unsafe/ambiguous manifest path component: " + repr(value))
    return value


def inventory(root: Path, excluded_manifest: Path):
    result = {}
    aliases = set()
    pending = [(root, "")]
    while pending:
        here, prefix = pending.pop()
        with os.scandir(here) as entries:
            for entry in entries:
                name = prefix + entry.name
                relative_name(name)
                st = entry.stat(follow_symlinks=False)
                if stat.S_ISLNK(st.st_mode) or reparse(st):
                    raise GuardError("symlink/reparse entries are not accepted: " + str(Path(entry.path)))
                path = Path(entry.path)
                if stat.S_ISDIR(st.st_mode):
                    pending.append((path, name + "/"))
                elif stat.S_ISREG(st.st_mode):
                    if path.resolve(strict=True) == excluded_manifest:
                        continue  # The pinned manifest envelope cannot hash itself.
                    if name.casefold() in aliases:
                        raise GuardError("case-insensitive file path collision: " + name)
                    aliases.add(name.casefold())
                    result[name] = path
                else:
                    raise GuardError("nonregular entry is not accepted: " + str(path))
    return result


def verify_tree(root: Path, manifest: Path, expected_pin: str, label: str):
    if not isinstance(expected_pin, str) or not HEX256.fullmatch(expected_pin):
        raise GuardError(label + " manifest pin must be a complete SHA256 hex string")
    ordinary_file(manifest)
    manifest = manifest.resolve(strict=True)
    raw = manifest.read_bytes()
    observed_pin = digest(raw)
    if observed_pin != expected_pin.lower():
        raise GuardError(label + " manifest SHA256 mismatch; expected=" + expected_pin.lower() + "; observed=" + observed_pin)
    try:
        payload = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=pairs_without_duplicates)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise GuardError(label + " manifest is not valid UTF-8 JSON: " + str(error)) from error
    if isinstance(payload, list):
        if label == "dependency":
            raise GuardError("dependency manifest requires an explicit complete flag and files table")
        files = payload
    elif isinstance(payload, dict):
        if label == "dependency" and (payload.get("complete") is not True or payload.get("missing") != []):
            raise GuardError("dependency snapshot is not explicitly complete or has recorded missing inputs")
        files = payload.get("files")
    else:
        files = None
    if not isinstance(files, list) or not files:
        raise GuardError(label + " manifest must contain a nonempty files table")
    expected = {}
    aliases = set()
    for row in files:
        if not isinstance(row, dict):
            raise GuardError(label + " manifest row is not an object")
        name = relative_name(row.get("path"))
        if name.casefold() in aliases:
            raise GuardError(label + " duplicate or case-aliased manifest path: " + name)
        aliases.add(name.casefold())
        wanted_hash, wanted_bytes = row.get("sha256"), row.get("bytes")
        if not isinstance(wanted_hash, str) or not HEX256.fullmatch(wanted_hash):
            raise GuardError(label + " invalid SHA256 for " + name)
        if type(wanted_bytes) is not int or wanted_bytes < 0:
            raise GuardError(label + " invalid byte count for " + name)
        full = root.joinpath(*name.split("/"))
        if not within(full.resolve(strict=False), root):
            raise GuardError(label + " path resolves outside root: " + name)
        if full.resolve(strict=False) == manifest:
            raise GuardError(label + " manifest cannot list its own pinned envelope as a payload file")
        expected[name] = (wanted_hash.lower(), wanted_bytes)
    actual = inventory(root, manifest)
    missing, extra = sorted(set(expected) - set(actual)), sorted(set(actual) - set(expected))
    if missing or extra:
        raise GuardError(label + " exact file set mismatch: " + json.dumps({"missing": missing, "extra": extra}, ensure_ascii=False))
    checked = []
    for name in sorted(expected):
        observed_hash, observed_bytes = file_hash(actual[name])
        wanted_hash, wanted_bytes = expected[name]
        if observed_hash != wanted_hash or observed_bytes != wanted_bytes:
            raise GuardError(label + " file identity mismatch: " + json.dumps({"path": name, "expected_sha256": wanted_hash, "observed_sha256": observed_hash, "expected_bytes": wanted_bytes, "observed_bytes": observed_bytes}, ensure_ascii=False))
        checked.append({"path": name, "sha256": observed_hash, "bytes": observed_bytes})
    return {"root": str(root), "manifest": str(manifest), "manifest_sha256": observed_pin,
            "exact_file_set": True, "file_count": len(checked), "checked": checked,
            "excluded_envelope": str(manifest) if within(manifest, root) else None}


def write_json(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def verify_runtime(root: Path, listed: set, event: dict):
    """Verify the enumerated active Python/numpy runtime, not an entire OS."""
    if RUNTIME_ENVIRONMENT not in listed:
        raise GuardError("runtime environment inventory must be listed in the pinned candidate manifest")
    path = root.joinpath(*RUNTIME_ENVIRONMENT.split("/"))
    raw = path.read_bytes()
    try:
        inventory_spec = json.loads(raw.decode("utf-8-sig"), object_pairs_hook=pairs_without_duplicates)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise GuardError("runtime environment inventory is not valid UTF-8 JSON: " + str(error)) from error
    if not isinstance(inventory_spec, dict) or inventory_spec.get("schema_version") != 1:
        raise GuardError("runtime environment inventory requires schema_version=1")
    python_spec, numpy_spec = inventory_spec.get("python"), inventory_spec.get("numpy")
    rows = inventory_spec.get("core_binary_hashes")
    if not isinstance(python_spec, dict) or not isinstance(numpy_spec, dict) or not isinstance(rows, list) or not rows:
        raise GuardError("runtime environment requires python, numpy and nonempty core_binary_hashes")
    report = {"inventory_path": str(path), "inventory_sha256": digest(raw), "matched": False,
              "scope": "only enumerated active Python/numpy versions and binary files; not complete stdlib/OS freezing",
              "absolute_provenance_paths_are_not_dynamic_locators": True,
              "rollback_environment_is_not_numeric_gate": True,
              "python": {"expected": python_spec, "observed_version": platform.python_version(),
                         "observed_version_info": list(sys.version_info), "observed_sys_version": sys.version,
                         "observed_executable": str(Path(sys.executable).resolve(strict=True))},
              "numpy": {"expected": numpy_spec}, "core_binary_checks": []}
    event["runtime_environment"] = report
    if python_spec.get("version") != report["python"]["observed_version"]:
        raise GuardError("runtime Python version mismatch")
    if python_spec.get("version_info") != report["python"]["observed_version_info"]:
        raise GuardError("runtime Python version_info mismatch")
    try:
        numpy = importlib.import_module("numpy")
        try:
            core = importlib.import_module("numpy._core._multiarray_umath")
        except ModuleNotFoundError:
            core = importlib.import_module("numpy.core._multiarray_umath")
    except ImportError as error:
        raise GuardError("required numpy runtime could not be imported: " + str(error)) from error
    numpy_package = Path(numpy.__file__).resolve(strict=True).parent
    active_core = Path(core.__file__).resolve(strict=True)
    python_executable = Path(sys.executable).resolve(strict=True)
    report["numpy"].update({"observed_version": numpy.__version__, "observed_package_file": str(Path(numpy.__file__).resolve(strict=True)),
                            "observed_multiarray_umath_file": str(active_core)})
    if numpy_spec.get("version") != numpy.__version__:
        raise GuardError("runtime numpy version mismatch")
    # Legacy top-level names are provenance aliases, but contradictory aliases
    # are rejected instead of silently selecting whichever is more convenient.
    for alias, version in (("python_version", python_spec["version"]), ("numpy_version", numpy_spec["version"])):
        if alias in inventory_spec and inventory_spec[alias] != version:
            raise GuardError("runtime inventory has contradictory version aliases: " + alias)
    seen, found_python, found_core = set(), False, False
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("role"), str) or not row["role"]:
            raise GuardError("runtime core_binary_hashes row requires a named role")
        locator = row.get("locator")
        if not isinstance(locator, dict):
            raise GuardError("runtime binary requires an explicit dynamic locator object")
        base = locator.get("base")
        if base == "python_executable":
            if set(locator) != {"base"}:
                raise GuardError("python_executable locator must not override its path")
            binary = python_executable
        elif base in ("numpy_package", "numpy_install_parent"):
            if set(locator) != {"base", "path"}:
                raise GuardError("numpy binary locator requires only base and path")
            relative = relative_name(locator["path"])
            if base == "numpy_install_parent" and not relative.startswith("numpy.libs/"):
                raise GuardError("numpy_install_parent binary must be inside the enumerated numpy.libs tree")
            binary_root = numpy_package if base == "numpy_package" else numpy_package.parent
            binary = binary_root.joinpath(*relative.split("/"))
            if not within(binary.resolve(strict=False), binary_root):
                raise GuardError("runtime binary locator escapes its dynamic base")
        else:
            raise GuardError("unknown runtime binary locator base: " + repr(base))
        ordinary_file(binary)
        binary = binary.resolve(strict=True)
        if str(binary).casefold() in seen:
            raise GuardError("duplicate runtime binary locator: " + str(binary))
        seen.add(str(binary).casefold())
        wanted_hash, wanted_bytes = row.get("sha256"), row.get("bytes")
        if not isinstance(wanted_hash, str) or not HEX256.fullmatch(wanted_hash) or type(wanted_bytes) is not int or wanted_bytes < 0:
            raise GuardError("runtime binary requires a complete SHA256 and byte count")
        observed_hash, observed_bytes = file_hash(binary)
        check = {"role": row["role"], "locator": locator, "observed_path": str(binary),
                 "expected_sha256": wanted_hash.lower(), "observed_sha256": observed_hash,
                 "expected_bytes": wanted_bytes, "observed_bytes": observed_bytes,
                 "matched": observed_hash == wanted_hash.lower() and observed_bytes == wanted_bytes}
        report["core_binary_checks"].append(check)
        if not check["matched"]:
            raise GuardError("runtime binary identity mismatch: " + row["role"])
        found_python = found_python or (base == "python_executable" and binary == python_executable and row["role"] == "python_executable")
        found_core = found_core or (binary == active_core and row["role"] == "numpy_multiarray_umath")
    if not found_python or not found_core:
        raise GuardError("runtime inventory must pin the active Python executable and imported numpy multiarray core")
    report["matched"] = True
    return report


def get_parser():
    parser = Parser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--dependency-root", required=True)
    parser.add_argument("--dependency-manifest", required=True)
    parser.add_argument("--dependency-manifest-sha256", required=True)
    parser.add_argument("--mode", required=True, choices=("research", "audit", "edit", "resume"))
    parser.add_argument("--out", required=True)
    return parser


def run(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    event = {"schema": "local-explicit-preflight-v4", "started_at_utc": utc(), "status": "FAIL",
             "full_preflight": False, "pre_execution_identity_passed": False, "child_events": [],
             "command": [sys.executable, str(Path(__file__).resolve()), *argv],
             "boundaries": {"native_role_installation": "not attempted or certified", "semantic_academic_certification": False,
                            "model_scoring": False, "numerical_scope": "synthetic toy identities only; not economic identification",
                            "dependency_scope": "only explicitly enumerated snapshot files, not the entire local knowledge base",
                            "manifest_identity": "caller-pinned SHA256, not a cryptographic signature",
                            "os_sandbox": False, "payload_execution": "only two enumerated numerical scripts after all identity checks"}}
    out = None
    stdout, stderr = [], []
    code = 2
    try:
        args = get_parser().parse_args(argv)
        event["mode"] = args.mode
        raw_root = Path(args.root).absolute()
        raw_dep = Path(args.dependency_root).absolute()
        proposed_out = Path(args.out).absolute().resolve(strict=False)
        # Output is external to both immutable input trees, including failed runs.
        for protected in (raw_root.resolve(strict=False), raw_dep.resolve(strict=False)):
            if within(proposed_out, protected) or within(protected, proposed_out):
                raise GuardError("output and protected input trees must be disjoint: " + str(proposed_out))
        if proposed_out.exists() or proposed_out.is_symlink():
            raise GuardError("output directory must be new and nonexistent: " + str(proposed_out))
        try:
            proposed_out.mkdir(parents=True, exist_ok=False)
        except FileExistsError as error:
            raise GuardError("output directory must be new and nonexistent: " + str(proposed_out)) from error
        # Bind only after exclusive creation. Existing/racing outputs are never
        # assigned to out and therefore never touched by exception/final writes.
        out = proposed_out
        if out.is_symlink() or reparse(out.lstat()):
            raise GuardError("output directory must not be a symlink/reparse point")
        root = directory(raw_root, "candidate root")
        dep = directory(raw_dep, "dependency root")
        if within(root, dep) or within(dep, root):
            raise GuardError("candidate and dependency roots must be disjoint")
        candidate_manifest = Path(args.manifest).absolute()
        dependency_manifest = Path(args.dependency_manifest).absolute()
        event["candidate"] = verify_tree(root, candidate_manifest, args.manifest_sha256, "candidate")
        event["dependency"] = verify_tree(dep, dependency_manifest, args.dependency_manifest_sha256, "dependency")
        listed = {entry["path"] for entry in event["candidate"]["checked"]}
        self_path = Path(__file__).resolve(strict=True)
        if self_path != root / "scripts" / "runtime_guard.py" or "scripts/runtime_guard.py" not in listed:
            raise GuardError("execute the manifest-listed guard from the bound candidate root")
        if any(name not in listed for name in CHECK_SCRIPTS):
            raise GuardError("both numerical scripts must be explicitly listed in the candidate manifest")
        verify_runtime(root, listed, event)
        event["pre_execution_identity_passed"] = True
        write_json(out / "event.json", event)
        for relative in CHECK_SCRIPTS:
            tag = Path(relative).stem
            result_path = out / (tag + ".json")
            command = [sys.executable, "-I", "-B", str(root.joinpath(*relative.split("/"))), "--out", str(result_path)]
            child = {"command": command, "cwd": str(out), "started_at_utc": utc(), "started": False,
                     "stdout_path": str(out / (tag + ".stdout.txt")), "stderr_path": str(out / (tag + ".stderr.txt"))}
            event["child_events"].append(child)
            write_json(out / "event.json", event)
            try:
                process = subprocess.Popen(command, cwd=str(out), stdin=subprocess.DEVNULL,
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
                child.update({"started": True, "pid": process.pid})
                write_json(out / "event.json", event)
                try:
                    child_stdout, child_stderr = process.communicate(timeout=120)
                    child["timed_out"] = False
                except subprocess.TimeoutExpired:
                    process.kill()
                    child_stdout, child_stderr = process.communicate()
                    child["timed_out"] = True
                child["exit_status"] = process.returncode
            except OSError as error:
                child_stdout, child_stderr = b"", (str(error) + "\n").encode("utf-8")
                child.update({"exit_status": None, "launch_error": repr(error)})
            Path(child["stdout_path"]).write_bytes(child_stdout)
            Path(child["stderr_path"]).write_bytes(child_stderr)
            child.update({"finished_at_utc": utc(), "literal_stdout": child_stdout.decode("utf-8", errors="replace"),
                          "literal_stderr": child_stderr.decode("utf-8", errors="replace"),
                          "stdout_sha256": digest(child_stdout), "stderr_sha256": digest(child_stderr)})
            if result_path.is_file():
                child["result_path"], child["result_sha256"] = str(result_path), file_hash(result_path)[0]
            write_json(out / "event.json", event)
            if not child["started"] or child["exit_status"] != 0 or child.get("timed_out"):
                raise GuardError("numerical child failed: " + tag, exit_code=3)
        event["post_execution_candidate"] = verify_tree(root, candidate_manifest, args.manifest_sha256, "candidate")
        event["post_execution_dependency"] = verify_tree(dep, dependency_manifest, args.dependency_manifest_sha256, "dependency")
        event["post_execution_runtime"] = verify_runtime(root, listed, event)
        event["status"], event["full_preflight"], code = "PASS", True, 0
        stdout.append(json.dumps({"status": "PASS", "mode": args.mode, "full_preflight": True,
                                  "candidate_files": event["candidate"]["file_count"],
                                  "dependency_files": event["dependency"]["file_count"],
                                  "numerical_child_exit_statuses": [c["exit_status"] for c in event["child_events"]],
                                  "event": str(out / "event.json"),
                                  "scope": "local explicit load identity + toy checks only"}, ensure_ascii=False) + "\n")
    except GuardError as error:
        code = error.exit_code
        event["error"] = str(error)
        stderr.append("runtime_guard: " + str(error) + "\n")
        stdout.append(json.dumps({"status": "FAIL", "full_preflight": False, "exit_status": code,
                                  "child_count": len(event["child_events"])}) + "\n")
    except Exception as error:
        code = 4
        event["error"], event["error_type"] = str(error), type(error).__name__
        stderr.append(traceback.format_exc())
        stdout.append(json.dumps({"status": "FAIL", "full_preflight": False, "exit_status": code,
                                  "child_count": len(event["child_events"])}) + "\n")
    event["finished_at_utc"], event["exit_status"] = utc(), code
    event["literal_stdout"], event["literal_stderr"] = "".join(stdout), "".join(stderr)
    if out is not None:
        try:
            (out / "stdout.txt").write_bytes(event["literal_stdout"].encode("utf-8"))
            (out / "stderr.txt").write_bytes(event["literal_stderr"].encode("utf-8"))
            write_json(out / "event.json", event)
        except OSError as error:
            code = 4
            stderr.append("runtime_guard: cannot write evidence: " + str(error) + "\n")
    sys.stdout.write("".join(stdout))
    sys.stderr.write("".join(stderr))
    return code


if __name__ == "__main__":
    raise SystemExit(run())
