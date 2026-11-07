import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

MAIN=Path(__file__).resolve().parents[1]/"starter"/"main.py"

def test_end_to_end(tmp_path):
    (tmp_path/"docs").mkdir()
    (tmp_path/"docs"/"ok.txt").write_text("ok")
    (tmp_path/"docs"/"index.md").write_text("[yes](ok.txt) [no](missing.txt) [web](https://example.com) [escape](../../secret.txt)")
    r=subprocess.run([sys.executable,str(MAIN),str(tmp_path)],capture_output=True,text=True,timeout=5)
    assert r.returncode==1,r.stderr
    assert json.loads(r.stdout)==[{"file":"docs/index.md","target":"../../secret.txt"},{"file":"docs/index.md","target":"missing.txt"}]


def test_root_relative_links_and_query_fragments(tmp_path):
    (tmp_path / "guide.md").write_text("guide", encoding="utf-8")
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text(
        "[root](/guide.md#intro) [relative](../guide.md?view=1) "
        "[fragment](#section) [email](mailto:test@example.org) "
        "[missing](/absent.md?x=1#part)",
        encoding="utf-8",
    )
    r = subprocess.run([sys.executable, str(MAIN), str(tmp_path)],
                       capture_output=True, text=True, timeout=5)
    assert r.returncode == 1, r.stderr
    assert json.loads(r.stdout) == [{"file": "docs/index.md", "target": "/absent.md?x=1#part"}]


def test_no_broken_links(tmp_path):
    (tmp_path / "ok.md").write_text("[self](ok.md) [web](https://example.org)",
                                    encoding="utf-8")
    r = subprocess.run([sys.executable, str(MAIN), str(tmp_path)],
                       capture_output=True, text=True, timeout=5)
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout) == []
