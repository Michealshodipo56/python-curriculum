"""Verify function assignments with isolated reference implementations.

Each temporary task contains the real learner-facing acceptance tests and a
reference implementation. No reference answers are committed to task folders.
"""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1] / "gauntlex" / "04-functions"
REFERENCES = {
    "035-sum-function": "def sum_two(a,b):\n return a+b\n",
    "036-absolute-function": "def absolute(n):\n return abs(n)\n",
    "037-factorial": "def factorial(n):\n result=1\n for i in range(2,n+1): result*=i\n return result\n",
    "038-palindrome": "def is_palindrome(text):\n return text==text[::-1]\n",
    "039-vowel-count": "def count_vowels(text):\n return sum(c.lower() in 'aeiou' for c in text)\n",
    "040-prime-check": "def is_prime(n):\n return n>=2 and all(n%i for i in range(2,int(n**0.5)+1))\n",
    "041-fibonacci": "def fibonacci(n):\n a,b=0,1\n for _ in range(n): a,b=b,a+b\n return a\n",
    "042-anagram": "def are_anagrams(a,b):\n return sorted(a)==sorted(b)\n",
    "043-flatten-once": "def flatten_once(groups):\n return [x for group in groups for x in group]\n",
    "044-first-unique": "def first_unique(text):\n return next((c for c in text if text.count(c)==1),None)\n",
    "045-chunk-list": "def chunks(items,size):\n return [items[i:i+size] for i in range(0,len(items),size)]\n",
    "046-gcd": "def gcd(a,b):\n while b: a,b=b,a%b\n return abs(a)\n",
}


def main():
    with tempfile.TemporaryDirectory(prefix="gauntlex-functions-") as tmp:
        for task, reference in REFERENCES.items():
            sandbox = Path(tmp) / task
            (sandbox / "starter").mkdir(parents=True)
            shutil.copytree(ROOT / task / "tests", sandbox / "tests")
            (sandbox / "starter" / "solution.py").write_text(reference, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(sandbox / "tests"), "-q", "--tb=short"],
                cwd=sandbox, capture_output=True, text=True, timeout=45,
            )
            if result.returncode:
                print(f"FAIL {task}: reference rejected")
                print((result.stdout + result.stderr)[-2500:])
                return 1
            print(f"PASS {task}: reference accepted")
    print("All twelve function reference contracts passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
