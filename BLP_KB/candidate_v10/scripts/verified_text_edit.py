#!/usr/bin/env python3
"""Exact UTF-8 byte replacement with observed execution, patch and SH rollback.

This executes an explicitly supplied command, not a sandbox. The original is
never a command target: BASELINE uses the sibling pristine copy. A fresh output
directory is mandatory; --resume reuses only this transaction's recorded inputs
and skips every completed operation. An interrupted, started child with unknown
exit status is never silently rerun or counted as successful.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import traceback
import time
import uuid


SCHEMA = "verified-exact-text-edit-v2"
RUNTIME = Path(__file__).absolute().parent.parent / "skills" / "blp-project-professor" / "references" / "runtime-environment.json"


class TransactionError(Exception):
    pass


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def absolute(value):
    # No Windows directory handle is opened by abspath. Reparse components are
    # checked explicitly below rather than guessed after a failed resolve().
    return Path(os.path.abspath(os.fspath(value)))


def ordinary_chain(path, final_directory=False, allow_missing=False):
    path = absolute(path)
    for item in reversed([path, *path.parents]):
        try:
            info = item.lstat()
        except FileNotFoundError:
            if allow_missing:
                continue
            raise
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise TransactionError("symlink/reparse path components are not accepted: " + str(item))
        if item != path or final_directory:
            if not stat.S_ISDIR(info.st_mode):
                raise TransactionError("not an ordinary directory: " + str(item))
        elif not stat.S_ISREG(info.st_mode):
            raise TransactionError("not an ordinary file: " + str(item))
    return path


def dump(path, data):
    # Retry only a transient Windows sharing/access error at the atomic commit.
    # Diagnostics are append-only and never use dump (avoids recursive failure).
    path = ordinary_chain(path, allow_missing=True)
    ordinary_chain(path.parent, final_directory=True)
    raw = (json.dumps(data, ensure_ascii=True, allow_nan=False, indent=2) + "\n").encode("utf-8")
    temp = path.with_name(path.name + ".tmp")
    ordinary_chain(temp, allow_missing=True)
    temp.write_bytes(raw)
    failures = []
    delays = (0.05, 0.1, 0.2)
    for attempt in range(1, 5):
        try:
            os.replace(temp, path)
        except OSError as exc:
            failures.append({"attempt": attempt, "at_utc": utc(), "errno": exc.errno,
                             "winerror": getattr(exc, "winerror", None), "error": str(exc)})
            retry = getattr(exc, "winerror", None) == 5 and attempt < 4
            event = {"path": str(path), "attempt": attempt, "failures": failures,
                     "status": "retry" if retry else "failed", "at_utc": utc()}
            with (path.parent / "ATOMIC_WRITE_DIAGNOSTICS.jsonl").open("a", encoding="utf-8") as log:
                log.write(json.dumps(event, ensure_ascii=True) + "\n")
            if not retry:
                raise
            time.sleep(delays[attempt - 1])
        else:
            if failures:
                with (path.parent / "ATOMIC_WRITE_DIAGNOSTICS.jsonl").open("a", encoding="utf-8") as log:
                    log.write(json.dumps({"path": str(path), "attempt": attempt,
                                         "failures": failures, "status": "success", "at_utc": utc()}) + "\n")
            return


def posix_path(path):
    value = str(absolute(path))
    if os.name == "nt":
        drive, tail = os.path.splitdrive(value)
        if len(drive) != 2 or drive[1] != ":":
            raise TransactionError("Git POSIX rollback requires a local drive path, not UNC: " + value)
        return "/" + drive[0].lower() + tail.replace("\\", "/")
    return value


def checked_runtime(path):
    path = ordinary_chain(path)
    spec = json.loads(path.read_bytes().decode("utf-8-sig"))
    environment = spec.get("rollback_environment", {})
    rows = environment.get("executables", [])
    names, checks = {}, []
    for row in rows:
        name = row.get("name")
        if name not in {"sh", "git", "dirname", "cp"}:
            continue
        if name in names:
            raise TransactionError("duplicate rollback executable registration: " + str(name))
        binary = ordinary_chain(row["absolute_path"])
        raw = binary.read_bytes()
        if sha(raw) != row.get("sha256") or len(raw) != row.get("bytes"):
            raise TransactionError("registered rollback executable identity mismatch: " + str(binary))
        names[name] = str(binary)
        checks.append({"name": name, "path": str(binary), "sha256": sha(raw), "bytes": len(raw)})
    if set(names) != {"sh", "git", "dirname", "cp"}:
        raise TransactionError("runtime must register actual sh, git, dirname and cp binaries")
    entries = environment.get("path_entries")
    if not isinstance(entries, list) or not entries or any(not isinstance(p, str) or not Path(p).is_absolute() for p in entries):
        raise TransactionError("rollback PATH must have registered absolute path_entries")
    checked_dirs = [str(ordinary_chain(p, final_directory=True)) for p in entries]
    for name in ("dirname", "cp"):
        if os.path.normcase(str(Path(names[name]).parent)) not in {os.path.normcase(p) for p in checked_dirs}:
            raise TransactionError("actual " + name + " directory is missing from the registered rollback PATH")
    env = dict(os.environ)
    # Neither outer repository discovery nor user/system Git settings may leak
    # into the disposable patch repositories. No command uses an outer index.
    for key in list(env):
        if key.upper().startswith("GIT_"):
            del env[key]
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                "GIT_CONFIG_SYSTEM": os.devnull, "GIT_TERMINAL_PROMPT": "0",
                "GIT_DISCOVERY_ACROSS_FILESYSTEM": "0", "GIT_OPTIONAL_LOCKS": "0",
                "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C"})
    env["PATH"] = os.pathsep.join(checked_dirs + [env.get("PATH", "")])
    return names, env, {"inventory": str(path), "inventory_sha256": sha(path.read_bytes()),
                        "executables": checks, "path_entries": checked_dirs,
                        "git_config_isolation": True, "scope": "enumerated binaries only, not a frozen OS"}


class Transaction:
    def __init__(self, args):
        self.args, self.out, self.ledger = args, None, None
        self.path = absolute(args.out)
        self.ledger_path = self.path / "VERIFICATION.txt"

    def save(self):
        self.ledger["updated_at_utc"] = utc()
        dump(self.ledger_path, self.ledger)

    def step(self, key, operation):
        if key in self.ledger["completed_steps"]:
            return
        self.ledger["next_executable_action"] = key
        self.save()
        operation()
        self.ledger["completed_steps"].append(key)
        self.ledger["state_transitions"].append({"step": key, "completed_at_utc": utc()})
        self.save()

    def assert_source(self):
        ordinary_chain(self.source)
        raw = self.source.read_bytes()
        if sha(raw) != self.ledger["binding"]["source_sha256"]:
            raise TransactionError("original source hash changed; refusing to continue")
        self.ledger["source_hash_checks"].append({"at_utc": utc(), "sha256": sha(raw), "unchanged": True})

    def assert_completed_artifacts(self):
        """A committed step is not permission to trust subsequently changed bytes.

        Validate, do not repair or rerun completed commands. This guards ordinary
        drift against the recorded binding, not an adversary rewriting the ledger.
        """
        done = set(self.ledger["completed_steps"])
        def exact(path, expected):
            if ordinary_chain(path).read_bytes() != expected:
                raise TransactionError("completed artifact bytes changed: " + str(path))
        def hashed(path, expected):
            if not expected or sha(ordinary_chain(path).read_bytes()) != expected:
                raise TransactionError("completed artifact hash changed: " + str(path))
        if "PREPARE" in done:
            exact(self.pristine_file, self.pristine)
            hashed(self.rollback, self.ledger["hashes"].get("ROLLBACK"))
        if "WRITE_MODIFIED" in done:
            exact(self.modified, self.modified_bytes)
        if "PATCH_DIFF" in done:
            hashed(self.diff, self.ledger["hashes"].get("DIFF_FILE"))
        if "VERIFY_PATCH" in done:
            exact(self.apply_repo / self.modified.name, self.modified_bytes)
        events = self.ledger["command_execution"]
        if "ROLLBACK_SH" in done:
            exact(self.rollback_target, self.pristine)
        elif "PREPARE_ROLLBACK_COPY" in done:
            successful = any(e["step"] == "ROLLBACK_SH" and e.get("finished") and e.get("exit_status") == 0 for e in events)
            exact(self.rollback_target, self.pristine if successful else self.modified_bytes)
        for event in events:
            if event.get("finished"):
                for channel in ("stdout", "stderr"):
                    hashed(Path(event[channel + "_path"]), event.get(channel + "_sha256"))
        if "FINALIZE" in done:
            for role, path in self.roles.items():
                if role != "VERIFICATION":
                    recorded = self.ledger["reopened_roles"].get(role, {})
                    if recorded.get("absolute_path") != str(path):
                        raise TransactionError("completed role binding changed: " + role)
                    hashed(path, recorded.get("sha256"))
        self.ledger.setdefault("artifact_integrity_checks", []).append({"at_utc": utc(), "completed_steps_checked": len(done), "matched": True})

    def command(self, key, command, cwd, env, required_zero=False):
        prior = [event for event in self.ledger["command_execution"] if event["step"] == key]
        if prior and not prior[-1].get("finished"):
            raise TransactionError("started child has unknown outcome; reconcile it before resuming: " + key)
        if prior and prior[-1]["started"] and prior[-1]["finished"] and type(prior[-1].get("exit_status")) is int and not prior[-1].get("timed_out") and (not required_zero or prior[-1]["exit_status"] == 0):
            # Persisted child completion outranks the small gap before the
            # containing step's commit; BASELINE/MODIFIED are never rerun.
            event = prior[-1]
            if event["command"] != command or event["cwd"] != str(cwd):
                raise TransactionError("completed child binding differs on resume: " + key)
            return event
        attempt = len(prior) + 1
        stem = key + "." + str(attempt)
        stdout_file, stderr_file = self.path / "streams" / (stem + ".stdout.bin"), self.path / "streams" / (stem + ".stderr.bin")
        event = {"kind": "command_execution", "step": key, "attempt": attempt,
                 "command": command, "cwd": str(cwd), "stdin": "DEVNULL (same empty input for all behavior commands)",
                 "started_at_utc": utc(), "started": False, "finished": False,
                 "pid": None, "exit_status": None, "stdout_path": str(stdout_file), "stderr_path": str(stderr_file)}
        self.ledger["command_execution"].append(event)
        self.save()
        with stdout_file.open("xb") as stdout, stderr_file.open("xb") as stderr:
            try:
                process = subprocess.Popen(command, cwd=str(cwd), env=env, stdin=subprocess.DEVNULL,
                                           stdout=stdout, stderr=stderr, shell=False)
                event.update({"started": True, "pid": process.pid})
                try:
                    self.save()
                except OSError as error:
                    event["persistence_error"] = {"type": type(error).__name__, "message": str(error),
                                                  "errno": error.errno, "winerror": getattr(error, "winerror", None)}
                    # Launch succeeded. Never turn a PID-commit failure into a
                    # launch failure or a finished child with an unknown exit.
                    raise TransactionError("started child PID persistence failed; reconcile before resume: " + key) from error
                try:
                    event["exit_status"] = process.wait(timeout=self.args.timeout)
                    event["timed_out"] = False
                except subprocess.TimeoutExpired:
                    process.kill()
                    event["exit_status"] = process.wait()
                    event["timed_out"] = True
            except OSError as error:
                if event["started"]:
                    event["execution_error"] = {"type": type(error).__name__, "message": str(error),
                                                "errno": error.errno, "winerror": getattr(error, "winerror", None)}
                    raise TransactionError("started child outcome is unknown; reconcile before resume: " + key) from error
                event["launch_error"] = {"type": type(error).__name__, "message": str(error),
                                         "errno": error.errno, "winerror": getattr(error, "winerror", None)}
                # A launch failure is not child stderr and never gets a fake
                # PID, child exit code, or evaluator outcome.
            finally:
                stdout.flush()
                stderr.flush()
        if event["started"] and type(event.get("exit_status")) is not int:
            raise TransactionError("started child has no observed integer exit; refusing completion: " + key)
        raw_stdout, raw_stderr = stdout_file.read_bytes(), stderr_file.read_bytes()
        event.update({"finished": True, "finished_at_utc": utc(),
                      "literal_stdout": raw_stdout.decode("utf-8", errors="replace"),
                      "literal_stderr": raw_stderr.decode("utf-8", errors="replace"),
                      "stdout_sha256": sha(raw_stdout), "stderr_sha256": sha(raw_stderr),
                      "stdout_bytes": len(raw_stdout), "stderr_bytes": len(raw_stderr)})
        self.save()
        if not event["started"] or event.get("timed_out") or required_zero and event["exit_status"] != 0:
            raise TransactionError("command did not complete the required operation: " + key)
        return event

    def behavior(self, label, target):
        self.assert_source()
        expected = self.pristine if label != "MODIFIED" else self.modified_bytes
        if target.read_bytes() != expected:
            raise TransactionError("behavior input no longer matches its recorded bytes: " + label)
        command = [str(target) if item == "{TARGET}" else item for item in self.template]
        event = self.command(label, command, self.cwd, self.env)
        if not event.get("started") or not event.get("finished") or type(event.get("exit_status")) is not int:
            raise TransactionError("behavior requires an observed completed child: " + label)
        if target.read_bytes() != expected:
            raise TransactionError("behavior command modified its target bytes: " + label)
        self.assert_source()
        self.ledger["behaviors"][label] = {k: event[k] for k in ("command", "cwd", "pid", "exit_status", "literal_stdout", "literal_stderr", "stdout_path", "stderr_path", "stdout_sha256", "stderr_sha256")}
        self.ledger["behaviors"][label]["target_sha256"] = sha(expected)

    def git(self, key, repo, args):
        env = dict(self.env)
        env["GIT_CEILING_DIRECTORIES"] = str(self.path)
        command = [self.tools["git"], "--git-dir=" + str(repo / ".git"), "--work-tree=" + str(repo),
                   "-c", "core.autocrlf=false", "-c", "core.safecrlf=false", "-c", "core.filemode=false",
                   "-c", "core.attributesfile=" + os.devnull, *args]
        return self.command(key, command, repo, env, required_zero=True)

    def prepare(self):
        for directory in (self.path / "streams", self.cwd):
            directory.mkdir(exist_ok=True)
            ordinary_chain(directory, final_directory=True)
        if self.pristine_file.exists():
            if ordinary_chain(self.pristine_file).read_bytes() != self.pristine:
                raise TransactionError("incomplete preparation has unexpected pristine bytes")
        else:
            self.pristine_file.write_bytes(self.pristine)
        # Both utility names are resolved from the checked full POSIX PATH.
        # The script has no Python/Git dependency and remains usable elsewhere
        # with any ordinary POSIX sh, dirname and cp installation.
        script = ("#!/bin/sh\nset -eu\n"
                  "if [ \"$#\" -ne 1 ]; then printf '%s\\n' 'usage: ROLLBACK.sh TARGET_COPY' >&2; exit 2; fi\n"
                  "here=$(CDPATH= cd -P \"$(dirname \"$0\")\" && pwd)\n"
                  "case $1 in /*) destination=$1 ;; *) destination=$PWD/$1 ;; esac\n"
                  "cp \"$here/" + self.pristine_file.name + "\" \"$destination\"\n"
                  "printf '%s\\n' 'restored pristine bytes'\n")
        self.rollback.write_bytes(script.encode("utf-8"))
        self.ledger["hashes"]["ROLLBACK"] = sha(script.encode("utf-8"))
        self.rollback.chmod(0o755)
        self.ledger["rollback_executable"] = {"requested_mode": "0755", "observed_mode": oct(stat.S_IMODE(self.rollback.stat().st_mode)),
                                                "windows_note": "Windows does not retain POSIX executable mode; actual SH execution is independently recorded" if os.name == "nt" else None}

    def write_modified(self):
        self.modified.write_bytes(self.modified_bytes)
        self.modified.chmod(stat.S_IMODE(self.source.stat().st_mode))
        self.ledger["hashes"]["MODIFIED_FILE"] = sha(self.modified_bytes)

    def prepare_patch_repo(self):
        self.patch_repo.mkdir(exist_ok=True)
        ordinary_chain(self.patch_repo, final_directory=True)
        (self.patch_repo / self.modified.name).write_bytes(self.pristine)
        (self.patch_repo / ".gitattributes").write_bytes(b"* -text -diff\n")

    def make_patch(self):
        (self.patch_repo / self.modified.name).write_bytes(self.modified_bytes)
        event = self.git("PATCH_DIFF", self.patch_repo, ["diff", "--binary", "--full-index", "--no-ext-diff", "--no-textconv", "--", self.modified.name])
        raw = Path(event["stdout_path"]).read_bytes()
        if b"GIT binary patch" not in raw:
            raise TransactionError("Git did not emit the requested binary patch")
        self.diff.write_bytes(raw)
        self.ledger["hashes"]["DIFF_FILE"] = sha(raw)

    def prepare_apply_repo(self):
        self.apply_repo.mkdir(exist_ok=True)
        ordinary_chain(self.apply_repo, final_directory=True)
        (self.apply_repo / self.modified.name).write_bytes(self.pristine)

    def verify_patch(self):
        restored = (self.apply_repo / self.modified.name).read_bytes()
        if restored != self.modified_bytes:
            raise TransactionError("git apply did not reconstruct exact MODIFIED_FILE bytes")
        self.ledger["patch_verification"] = {"exact_bytes": True, "sha256": sha(restored),
                                            "target_name": self.modified.name, "how_to_apply": "place original bytes at target_name; git apply DIFF_FILE.patch in that directory"}

    def rollback_copy(self):
        self.rollback_target.write_bytes(self.modified_bytes)
        self.ledger["rollback_input_sha256"] = sha(self.rollback_target.read_bytes())

    def rollback_sh(self):
        self.command("ROLLBACK_SH", [self.tools["sh"], posix_path(self.rollback), posix_path(self.rollback_target)], self.path, self.env, required_zero=True)
        restored = self.rollback_target.read_bytes()
        if restored != self.pristine:
            raise TransactionError("SH rollback did not restore exact pristine bytes")
        self.ledger["rollback_restoration"] = {"sha256": sha(restored), "original_sha256": sha(self.pristine), "matched": True}

    def finalize(self):
        self.assert_source()
        baseline, rollback = self.ledger["behaviors"]["BASELINE"], self.ledger["behaviors"]["ROLLBACK"]
        matches = all(baseline[key] == rollback[key] for key in ("exit_status", "stdout_sha256", "stderr_sha256"))
        self.ledger["rollback_behavior_matches_baseline"] = matches
        if not matches:
            raise TransactionError("restored behavior differs from BASELINE (bytes are separately verified)")
        # Reapply GOAL after rollback verification, never replacing this role
        # with the separately restored test copy.
        # Already separate from the restored copy; retain GOAL without trying
        # to rewrite a read-only copy inherited from an immutable source.
        if self.modified.read_bytes() != self.modified_bytes:
            raise TransactionError("final MODIFIED_FILE bytes do not match GOAL")
        if self.pristine_file.read_bytes() != self.pristine:
            raise TransactionError("sibling pristine bytes were changed")
        for role, path in self.roles.items():
            if role == "VERIFICATION":
                continue
            ordinary_chain(path)
            self.ledger["reopened_roles"][role] = {"absolute_path": str(path), "sha256": sha(path.read_bytes()), "bytes": path.stat().st_size}
        # Reopen the native JSON ledger too; its self hash cannot be embedded in
        # itself. The final printed receipt supplies that post-write hash.
        json.loads(self.ledger_path.read_bytes().decode("utf-8"))
        self.ledger["reopened_roles"]["VERIFICATION"] = {"absolute_path": str(self.ledger_path), "native_json_reopened": True}

    def run(self):
        # Bind out exclusively before recording failed input checks. Existing
        # evidence is not assigned to self.out or altered on a rejected run.
        if self.args.resume:
            self.out = ordinary_chain(self.path, final_directory=True)
            self.ledger = json.loads(ordinary_chain(self.ledger_path).read_bytes().decode("utf-8"))
            if self.ledger.get("schema") != SCHEMA:
                raise TransactionError("output is not a compatible transaction")
            self.ledger["resume_events"].append({"at_utc": utc(), "invocation": sys.argv})
        else:
            ordinary_chain(self.path.parent, final_directory=True)
            self.path.mkdir(exist_ok=False)
            self.out = self.path
            self.ledger = {"schema": SCHEMA, "transaction_id": str(uuid.uuid4()), "started_at_utc": utc(),
                           "status": "IN_PROGRESS", "completed_steps": [], "state_transitions": [],
                           "command_execution": [], "behaviors": {}, "hashes": {}, "source_hash_checks": [],
                           "resume_events": [], "errors": [], "reopened_roles": {},
                           "next_executable_action": "VALIDATE_INPUTS_AND_RUNTIME",
                           "scope": "exact UTF-8 text bytes and supplied commands; not a sandbox, economic validation, or native role installation"}
            self.save()
        self.source = ordinary_chain(self.args.source)
        self.template = json.loads(self.args.command_json)
        if not isinstance(self.template, list) or not self.template or any(not isinstance(item, str) or not item or "\x00" in item for item in self.template):
            raise TransactionError("command-json must be a nonempty array of nonempty strings")
        if sum(item.count("{TARGET}") for item in self.template) != 1 or "{TARGET}" not in self.template:
            raise TransactionError("command-json requires exactly one complete {TARGET} argument")
        ordinary_chain(self.template[0])
        if not Path(self.template[0]).is_absolute():
            raise TransactionError("command executable must be an explicit absolute path")
        self.pristine = self.source.read_bytes()
        self.pristine.decode("utf-8", errors="strict")
        old, new = self.args.old.encode("utf-8"), self.args.new.encode("utf-8")
        if not old or old == new or b"\x00" in old + new + self.pristine:
            raise TransactionError("pure text replacement requires nonempty old, different new and no NUL bytes")
        hits, offset = [], 0
        while True:
            offset = self.pristine.find(old, offset)
            if offset < 0:
                break
            hits.append(offset)
            offset += 1  # Count overlapping matches, not bytes.count().
        if len(hits) != 1:
            raise TransactionError("old text must match exactly once; observed=" + str(len(hits)))
        self.modified_bytes = self.pristine[:hits[0]] + new + self.pristine[hits[0] + len(old):]
        suffix = self.source.suffix
        if any(c in suffix for c in "\r\n\"`$"):
            raise TransactionError("source suffix is not safe for a portable sibling rollback name")
        self.modified, self.pristine_file = self.path / ("MODIFIED_FILE" + suffix), self.path / ("PRISTINE" + suffix)
        self.diff, self.rollback = self.path / "DIFF_FILE.patch", self.path / "ROLLBACK.sh"
        self.rollback_target = self.path / ("ROLLBACK_COPY" + suffix)
        self.cwd, self.patch_repo, self.apply_repo = self.path / "command-cwd", self.path / "patch-build", self.path / "patch-apply"
        self.roles = {"MODIFIED_FILE": self.modified, "DIFF_FILE": self.diff, "VERIFICATION": self.ledger_path, "ROLLBACK": self.rollback}
        binding = {"source": str(self.source), "source_sha256": sha(self.pristine), "source_bytes": len(self.pristine),
                   "old": self.args.old, "new": self.args.new, "old_utf8_hex": old.hex(), "new_utf8_hex": new.hex(),
                   "match_byte_offset": hits[0], "command_template": self.template, "command_cwd": str(self.cwd),
                   "runtime_json": str(absolute(self.args.runtime_json)), "script_sha256": sha(Path(__file__).read_bytes())}
        if "binding" in self.ledger and self.ledger["binding"] != binding:
            raise TransactionError("resume arguments/source/script do not match the original binding")
        self.ledger["binding"], self.ledger["roles"] = binding, {k: str(v) for k, v in self.roles.items()}
        self.ledger["hashes"]["ORIGINAL"] = sha(self.pristine)
        self.tools, self.env, runtime = checked_runtime(self.args.runtime_json)
        if "runtime" in self.ledger and self.ledger["runtime"] != runtime:
            raise TransactionError("resume runtime identities differ from the recorded environment")
        self.ledger["runtime"] = runtime
        self.assert_completed_artifacts()
        self.ledger["status"] = "IN_PROGRESS"
        self.assert_source()
        self.step("PREPARE", self.prepare)
        self.step("BASELINE", lambda: self.behavior("BASELINE", self.pristine_file))
        self.step("WRITE_MODIFIED", self.write_modified)
        self.step("MODIFIED", lambda: self.behavior("MODIFIED", self.modified))
        self.step("PREPARE_PATCH", self.prepare_patch_repo)
        self.step("PATCH_INIT", lambda: self.git("PATCH_INIT", self.patch_repo, ["init", "--quiet"]))
        self.step("PATCH_INDEX_BASELINE", lambda: self.git("PATCH_INDEX_BASELINE", self.patch_repo, ["add", "--", self.modified.name]))
        self.step("PATCH_DIFF", self.make_patch)
        self.step("PREPARE_APPLY", self.prepare_apply_repo)
        self.step("APPLY_INIT", lambda: self.git("APPLY_INIT", self.apply_repo, ["init", "--quiet"]))
        self.step("PATCH_CHECK", lambda: self.git("PATCH_CHECK", self.apply_repo, ["apply", "--check", "--", str(self.diff)]))
        self.step("PATCH_APPLY", lambda: self.git("PATCH_APPLY", self.apply_repo, ["apply", "--binary", "--", str(self.diff)]))
        self.step("VERIFY_PATCH", self.verify_patch)
        self.step("PREPARE_ROLLBACK_COPY", self.rollback_copy)
        self.step("ROLLBACK_SH", self.rollback_sh)
        self.step("ROLLBACK", lambda: self.behavior("ROLLBACK", self.rollback_target))
        self.step("FINALIZE", self.finalize)
        self.assert_completed_artifacts()
        self.ledger.update({"status": "PASS", "next_executable_action": None, "finished_at_utc": utc(), "exit_status": 0})
        self.save()
        # Actually reopen every role after the final ledger update.
        receipt = {role: {"absolute_path": str(path), "sha256": sha(ordinary_chain(path).read_bytes()), "bytes": path.stat().st_size}
                   for role, path in self.roles.items()}
        json.loads(self.ledger_path.read_bytes().decode("utf-8"))
        return {"status": "PASS", "roles": receipt, "behaviors": {k: {"stdout": v["literal_stdout"], "stderr": v["literal_stderr"], "exit_status": v["exit_status"]} for k, v in self.ledger["behaviors"].items()}}


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--source", required=True)
    result.add_argument("--old", required=True)
    result.add_argument("--new", required=True)
    result.add_argument("--command-json", required=True)
    result.add_argument("--out", required=True)
    result.add_argument("--runtime-json", default=str(RUNTIME))
    result.add_argument("--timeout", type=float, default=120.0)
    result.add_argument("--resume", action="store_true", help="resume this exact transaction; completed steps are not rerun")
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    transaction = Transaction(args)
    try:
        if not 0 < args.timeout <= 3600:
            raise TransactionError("timeout must be positive, finite and at most 3600 seconds")
        result = transaction.run()
        print(json.dumps(result, ensure_ascii=True, allow_nan=False))
        return 0
    except Exception as error:
        event = {"at_utc": utc(), "type": type(error).__name__, "message": str(error),
                 "errno": getattr(error, "errno", None), "winerror": getattr(error, "winerror", None)}
        if transaction.out is not None and transaction.ledger is not None:
            transaction.ledger["errors"].append(event)
            transaction.ledger.update({"status": "FAIL", "exit_status": 2, "last_error": event})
            try:
                transaction.save()
            except OSError as evidence_error:
                event["evidence_write_error"] = repr(evidence_error)
        result = {"status": "FAIL", "exit_status": 2, "error": event,
                  "verification": str(transaction.ledger_path) if transaction.out is not None else None,
                  "next_executable_action": transaction.ledger.get("next_executable_action") if transaction.ledger else None,
                  "completed_steps": transaction.ledger.get("completed_steps", []) if transaction.ledger else []}
        print(json.dumps(result, ensure_ascii=True, allow_nan=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
