"""Read-only availability checks of original assignment URLs.

No substitutions, credentials, account creation, POSTs or deployments. Store
status/redirect/type and small structural facts, not remote page bodies.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import ssl
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
URLS = [
    "http://www.gutenberg.org/files/1112/1112.txt",
    "https://api.thecatapi.com/v1/breeds",
    "https://restcountries.eu/rest/v2/all",
    "https://archive.ics.uci.edu/ml/datasets.php",
    "http://www.bu.edu/president/boston-university-facts-stats/",
    "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States",
    "https://thirtydaysofpython-v1-final.herokuapp.com/",
    "https://thirtydayofpython-api.herokuapp.com/",
]

def check(url):
    request = urllib.request.Request(url, headers={"User-Agent": "CurriculumSourceReview/1.0"})
    result = {"url": url, "checked_at": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            body = response.read(2_000_001)
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"),
                          bytes_sampled=len(body), sample_truncated=len(body)>2_000_000)
            result["legacy_uci_selector_present"] = b'cellpadding="3"' in body if "uci.edu" in url else None
            if "thecatapi" in url:
                data = json.loads(body)
                result.update(records=len(data), first_record_keys=sorted(data[0]),
                              weight_shape=type(data[0].get("weight")).__name__,
                              life_span_shape=type(data[0].get("life_span")).__name__)
    except urllib.error.HTTPError as error:
        result.update(status=error.code, final_url=error.url, error=error.reason)
    except Exception as error:
        result.update(status=None, error=f"{type(error).__name__}: {error}")
    return result

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check, URLS))
    (ROOT / "review/external_resource_checks.json").write_text(json.dumps(results, indent=2)+"\n", encoding="utf-8")
    for row in results:
        print(row["url"], row["status"], row.get("error", row.get("final_url")))
