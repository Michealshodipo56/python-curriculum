# CSV ETL Pipeline

## Project brief and acceptance criteria
Run python main.py INPUT.csv OUTPUT.jsonl. CSV header id,name,amount_cents. Trim fields; require nonempty id/name and nonnegative integer amount. Skip invalid rows; deduplicate by id keeping first valid row. Write compact sorted-key JSONL in original order using temporary file and atomic replacement. Print compact sorted-key JSON {written:N,skipped:M}. Missing args exit 2.

## Deliverables
Implement in starter/main.py, add unit tests and document architecture. Python 3.11+ standard library only. No network services. Do not print debug output to stdout. Use parameterized SQL where applicable.

## Run
python -m pytest tests -q
