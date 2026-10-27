"""Check reviewed, side-effect-free reference examples against their prose.

Reference implementations are instructor evidence only, never task entries.
"""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises"
results = []
for stem in ["exercise-02-string-formatter", "exercise-03-temperature-converter", "exercise-04-input-parsing"]:
    reference = BASE / (stem + "-solution.py")
    spec = importlib.util.spec_from_file_location(stem.replace("-", "_"), reference)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = io.StringIO()
    with contextlib.redirect_stdout(output), contextlib.redirect_stderr(io.StringIO()):
        module.main()
    actual = output.getvalue().splitlines()
    text = (BASE / (stem + ".md")).read_text(encoding="utf-8")
    section = text.split("## Expected output", 1)[1].split("## Steps", 1)[0]
    block = re.search(r"```text\n(.*?)```", section, re.S).group(1).splitlines()
    expected = block[1:] if block[0].startswith("$ ") else block
    entry = {"task": stem, "reference": reference.relative_to(ROOT).as_posix(),
             "expected_matches_actual": expected == actual,
             "differences": [{"line": i + 1, "expected": exp, "actual": act,
                              "expected_length": len(exp), "actual_length": len(act)}
                             for i, (exp, act) in enumerate(zip(expected, actual)) if exp != act],
             "expected_line_count": len(expected), "actual_line_count": len(actual)}
    if stem.endswith("input-parsing"):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                module.describe(0, -1)
        except Exception as error:
            entry["zero_negative_exponent"] = {"exception": type(error).__name__, "message": str(error)}
    if stem.endswith("string-formatter"):
        entry["oversized_name_row_length"] = len(module.format_row("A" * 30, 1, 1.0))
    results.append(entry)
destination = ROOT / "review/c1_reference_checks.json"
destination.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2))
