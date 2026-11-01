"""Collects the ACCC's public merger registers for the ACCC review data set (data/regulators/).

Stage 1 (probe): fetches one page of the informal merger reviews list, one matter page, the
statements of issues page and one authorisations list page, and saves the raw HTML so the parser
can be written against the real page structure. Requests are paced at one every 3 seconds.
Usage: python3 -I tools/accc_register_crawl.py <out_dir>
"""
import os
import sys
import time
import urllib.error
import urllib.request

UA = "paper-portfolio research crawler (contact via github.com/cameronrodgernz-del)"
PAUSE = 3.0

PROBE = {
    "list_p0.html": "https://www.accc.gov.au/public-registers/browse-public-registers?f%5B0%5D=type%3Aacccgov_informal_merger_review",
    "list_p1.html": "https://www.accc.gov.au/public-registers/browse-public-registers?f%5B0%5D=type%3Aacccgov_informal_merger_review&page=1",
    "matter_apn.html": "https://www.accc.gov.au/public-registers/acquisitions-and-mergers-registers/public-informal-merger-reviews-register-2002-25/apn-outdoor-group-limited-proposed-merger-with-oohmedia-limited",
    "landing.html": "https://www.accc.gov.au/public-registers/mergers-and-acquisitions-registers/public-informal-merger-reviews-register-2002-25",
    "auth_list_p0.html": "https://www.accc.gov.au/public-registers/browse-public-registers?f%5B0%5D=type%3Aacccgov_merger_authorisation",
}


def get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")[:5000]
    except (urllib.error.URLError, TimeoutError) as e:
        return -1, str(e)


def main(out: str) -> None:
    os.makedirs(out, exist_ok=True)
    log = []
    for name, url in PROBE.items():
        code, body = get(url)
        log.append(f"{code}\t{len(body)}\t{name}\t{url}")
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(body)
        if code in (403, 429):
            log.append("stopped: site refused automated access")
            break
        time.sleep(PAUSE)
    with open(os.path.join(out, "probe_log.tsv"), "w", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")


if __name__ == "__main__":
    main(sys.argv[1])
