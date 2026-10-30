# Markdown Link Checker

## Project brief and acceptance criteria
Run python main.py ROOT. Recursively inspect Markdown files. Extract inline links [label](target) where target has no spaces or parentheses. Ignore http:, https:, mailto:, and # links. Remove query/fragment from local targets. Resolve relative to containing file; targets beginning / resolve under ROOT. Flag missing files and paths escaping ROOT, including symlinks. Print compact sorted-key JSON array {file,target} sorted by file and target. Exit 1 for broken links, else 0. Never make network requests.

## Deliverables
Implement in starter/main.py, add unit tests and document architecture. Python 3.11+ standard library only. No network services. Do not print debug output to stdout. Use parameterized SQL where applicable.

## Run
python -m pytest tests -q
