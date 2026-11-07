"""Exercise algorithm contracts against temporary reference code and incomplete starters."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1] / "gauntlex" / "05-algorithms"
REFERENCES = {
    "047-word-count": "def word_count(text):\n return len(text.split())\n",
    "048-longest-word": "def longest_word(text):\n return max(text.split(),key=len,default='')\n",
    "049-rotate-list": "def rotate_right(items,k):\n return items[-(k%len(items)):] + items[:-(k%len(items))] if items and k%len(items) else list(items)\n",
    "050-merge-sorted": "def merge_sorted(left,right):\n return sorted(left+right)\n",
    "051-balanced-brackets": "def balanced_brackets(text):\n stack=[]\n pairs={')':'(',']':'[','}':'{'}\n for c in text:\n  if c in '([{': stack.append(c)\n  elif not stack or stack.pop()!=pairs[c]: return False\n return not stack\n",
    "052-run-length": "def run_length(text):\n result=[]\n for c in text:\n  if result and result[-1][0]==c: result[-1][1]+=1\n  else: result.append([c,1])\n return result\n",
    "053-caesar": "def caesar(text,k):\n out=[]\n for c in text:\n  base=65 if 'A'<=c<='Z' else 97 if 'a'<=c<='z' else None\n  out.append(chr(base+(ord(c)-base+k)%26) if base is not None else c)\n return ''.join(out)\n",
    "054-common-prefix": "def common_prefix(words):\n if not words: return ''\n prefix=words[0]\n for word in words[1:]:\n  while not word.startswith(prefix): prefix=prefix[:-1]\n return prefix\n",
    "055-matrix-transpose": "def transpose(matrix):\n return [list(row) for row in zip(*matrix)]\n",
    "056-binary-search": "def binary_search(items,target):\n low,high=0,len(items)-1\n while low<=high:\n  mid=(low+high)//2\n  if items[mid]==target: return mid\n  if items[mid]<target: low=mid+1\n  else: high=mid-1\n return -1\n",
    "057-second-largest": "def second_largest(items):\n values=sorted(set(items))\n return values[-2] if len(values)>1 else None\n",
    "058-group-by-length": "def group_by_length(words):\n result={}\n for word in words: result.setdefault(len(word),[]).append(word)\n return result\n",
    "059-valid-parentheses": "def valid_parentheses(text):\n depth=0\n for c in text:\n  depth+=1 if c=='(' else -1\n  if depth<0: return False\n return depth==0\n",
    "060-move-zeros": "def move_zeros(items):\n return [x for x in items if x!=0]+[0]*sum(x==0 for x in items)\n",
    "061-pascal-row": "def pascal_row(n):\n row=[1]\n for _ in range(n): row=[1]+[row[i]+row[i+1] for i in range(len(row)-1)]+[1]\n return row\n",
    "062-flatten-recursive": "def flatten_recursive(items):\n result=[]\n for item in items:\n  if isinstance(item,list): result.extend(flatten_recursive(item))\n  else: result.append(item)\n return result\n",
}


def run(tests, cwd):
    return subprocess.run(
        [sys.executable, "-m", "pytest", str(tests), "-q", "--tb=short"],
        capture_output=True, text=True, timeout=45, cwd=cwd,
    )


def main():
    actual = {path.name for path in ROOT.glob("[0-9][0-9][0-9]-*")}
    if actual != set(REFERENCES):
        print("Algorithm tasks and references differ:", sorted(actual ^ set(REFERENCES)))
        return 1
    with tempfile.TemporaryDirectory(prefix="gauntlex-algorithms-") as tmp:
        for name, reference in REFERENCES.items():
            task = ROOT / name
            starter_result = run(task / "tests", ROOT)
            output = starter_result.stdout + starter_result.stderr
            if starter_result.returncode != 1 or " failed" not in output or "ERROR " in output:
                print(f"FAIL {name}: incomplete starter not correctly rejected")
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
    print(f"All {len(REFERENCES)} algorithm contracts verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
