"""Print full Markdown teaching text/code, abbreviating rendered HTML tables.

Tables are presentation of example outputs, not silently interpreted as tasks.
Original files are byte-inventoried; this view is a semantic review aid.
"""
from pathlib import Path
import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[1]
for name in sys.argv[1:]:
    path = root / name
    text = path.read_text(encoding="utf-8-sig")
    def table_note(match):
        table = match[0]
        headers = re.findall(r"<th[^>]*>(.*?)</th>", table, re.S)
        return "[Rendered example output table: " + str(len(re.findall(r"<tr\b",table))) + " rows; headers " + repr(headers) + ". Inspect original for all rendered cell values.]"
    text = re.sub(r"<table\b.*?</table>", table_note, text, flags=re.S)
    print(f"===== {name} =====\n{text}")
