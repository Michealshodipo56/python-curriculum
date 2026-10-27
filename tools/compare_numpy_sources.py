"""Compare actual tutorial bodies and print every difference for review."""
from pathlib import Path
import difflib
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[1] / "30-Days-Of-Python"
a = (root / "24_Day_Statistics/24_statistics.md").read_text(encoding="utf-8")
b = (root / "numpy.md").read_text(encoding="utf-8")
def code(text):
    return re.findall(r"^```(?:python|py|p)\s*\n(.*?)^```", text, re.M|re.S)
aa, bb = code(a), code(b)
print("Python-tagged blocks:", len(aa), len(bb), "identical:", aa == bb)
for line in difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile="Day24", tofile="numpy.md", n=2):
    print(line)
