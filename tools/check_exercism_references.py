"""Run original Exercism tests against original instructor references in memory.

Learner stubs are not overwritten, and expected unfinished-stub failures are
never confused with broken source tests. No answers are written to assignments.
"""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]

def one(folder_name: str):
    import pytest
    folder = ROOT / folder_name
    metadata = json.loads((folder / ".meta/config.json").read_text(encoding="utf-8"))
    files = metadata["files"]
    references = files.get("exemplar", files.get("example", []))
    targets = files.get("solution", [])
    if len(references) != 1 or len(targets) != 1:
        print("UNSUPPORTED REFERENCE LAYOUT", references, targets)
        return 8
    reference = folder / references[0]
    name = Path(targets[0]).stem
    sys.path.insert(0, str(folder))
    spec = importlib.util.spec_from_file_location(name, reference)
    if spec is None or spec.loader is None: return 8
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return int(pytest.main([*[str(folder / name) for name in files["test"]], "-q", "--disable-warnings", "-p", "no:cacheprovider", "-o", "addopts="]))

if __name__ == "__main__":
    if len(sys.argv) == 2: raise SystemExit(one(sys.argv[1]))
    units = json.loads((ROOT / "review/candidates.json").read_text(encoding="utf-8"))
    results = []
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1", "PYTHONUTF8": "1"}
    for unit in units:
        if not unit["kind"].startswith("exercism-"): continue
        start = time.monotonic()
        try:
            result = subprocess.run([sys.executable, str(Path(__file__).resolve()), unit["folder"]], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", timeout=45)
            row = {"path": unit["path"], "exit_code": result.returncode, "result": result.stdout[-6000:], "stderr": result.stderr[-2000:], "duration_seconds": round(time.monotonic()-start, 2)}
        except subprocess.TimeoutExpired:
            row = {"path": unit["path"], "exit_code": 124, "result": "45-second isolated reference-test timeout"}
        results.append(row)
        print(len(results), unit["metadata"]["slug"], row["exit_code"], flush=True)
        (ROOT / "review/exercism_test_results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
