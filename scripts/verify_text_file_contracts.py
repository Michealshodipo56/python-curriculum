"""Verify text/file assignment tests accept reference code and reject empty starters."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1] / "gauntlex" / "06-text-files"
REFERENCES = {
    "063-normalize-spaces": "def normalize_spaces(text):\n return ' '.join(text.split())\n",
    "064-line-count": "def line_count(text):\n return len(text.splitlines())\n",
    "065-safe-integer": "def parse_integer(text):\n try: return int(text.strip(),10)\n except ValueError: return None\n",
    "066-extract-numbers": "import re\ndef extract_numbers(text):\n return [int(x) for x in re.findall(r'[0-9]+',text)]\n",
    "067-mask-email": "def mask_email(email):\n local,domain=email.split('@')\n return local[0]+'*'*(len(local)-1)+'@'+domain\n",
    "068-slugify": "import re\ndef slugify(text):\n return re.sub(r'[^a-z0-9]+','-',text.lower()).strip('-')\n",
    "069-csv-row": "import csv\ndef parse_csv_row(line):\n return next(csv.reader([line]))\n",
    "070-json-value": "import json\ndef json_value(text,key):\n return json.loads(text).get(key)\n",
    "071-json-compact": "import json\ndef compact_json(value):\n return json.dumps(value,sort_keys=True,separators=(',',':'))\n",
    "072-path-extension": "from pathlib import PurePosixPath\ndef path_extension(path):\n return PurePosixPath(path).suffix.lstrip('.').lower()\n",
    "073-safe-divide": "def safe_divide(a,b):\n return a/b if b else None\n",
    "074-parse-date": "from datetime import date\ndef parse_date(text):\n try:\n  value=date.fromisoformat(text)\n  return value.isoformat() if len(text)==10 else None\n except ValueError: return None\n",
    "075-days-between": "from datetime import date\ndef days_between(a,b):\n return abs((date.fromisoformat(a)-date.fromisoformat(b)).days)\n",
    "076-iso-weekday": "from datetime import date\ndef iso_weekday(text):\n return date.fromisoformat(text).isoweekday()\n",
    "077-clean-records": "def clean_records(records):\n return [{**record,'name':record['name'].strip()} for record in records if isinstance(record.get('name'),str) and record['name'].strip()]\n",
    "078-count-file-lines": "from pathlib import Path\ndef count_file_lines(path):\n return len(Path(path).read_text(encoding='utf-8').splitlines())\n",
    "079-read-json-file": "import json\nfrom pathlib import Path\ndef read_json_file(path):\n return json.loads(Path(path).read_text(encoding='utf-8'))\n",
    "080-csv-column-total": "import csv\ndef csv_column_total(path,column):\n with open(path,encoding='utf-8',newline='') as file:\n  rows=csv.DictReader(file)\n  total=0\n  for row in rows:\n   try: total+=int(row[column])\n   except (ValueError,TypeError): pass\n  return total\n",
}


def run(tests, cwd):
    return subprocess.run(
        [sys.executable, "-m", "pytest", str(tests), "-q", "--tb=short"],
        capture_output=True, text=True, timeout=45, cwd=cwd,
    )


def main():
    actual = {path.name for path in ROOT.glob("[0-9][0-9][0-9]-*")}
    if actual != set(REFERENCES):
        print("Missing or extra reference assignments:", sorted(actual ^ set(REFERENCES)))
        return 1
    with tempfile.TemporaryDirectory(prefix="gauntlex-text-files-") as tmp:
        for name, reference in REFERENCES.items():
            task = ROOT / name
            starter_result = run(task / "tests", ROOT)
            output = starter_result.stdout + starter_result.stderr
            if starter_result.returncode != 1 or " failed" not in output or "ERROR " in output:
                print(f"FAIL {name}: incomplete starter not rejected")
                print(output[-2000:])
                return 1
            sandbox = Path(tmp) / name
            (sandbox / "starter").mkdir(parents=True)
            shutil.copytree(task / "tests", sandbox / "tests")
            (sandbox / "starter" / "solution.py").write_text(reference, encoding="utf-8")
            result = run(sandbox / "tests", sandbox)
            if result.returncode:
                print(f"FAIL {name}: reference rejected")
                print((result.stdout + result.stderr)[-2500:])
                return 1
            print(f"PASS {name}: starter rejected, reference accepted")
    print(f"All {len(REFERENCES)} text/file contracts verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
