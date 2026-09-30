# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
"""Fetch the Hong Kong Observatory daily rainfall CSV once.

    uv run fetch.py

The saved file is the Observatory's response, including its headings,
completeness codes, and notes. Remove it only when you intentionally want to
fetch a newer snapshot.
"""

from pathlib import Path

import requests

URL = "https://data.weather.gov.hk/weatherAPI/cis/csvfile/HKO/2026/daily_HKO_RF_2026.csv"
FILE = "daily_HKO_RF_2026.csv"
HERE = Path(__file__).parent
DATA = HERE / "data"


def fetch(url: str, path: Path) -> Path:
    """Save the published CSV without changing its contents."""
    if path.exists():
        print(f"data/{path.name} is already here; delete it to fetch again.")
        return path
    path.parent.mkdir(exist_ok=True)
    print(f"Requesting {url}")
    reply = requests.get(url, timeout=60, headers={"User-Agent": "SD5913 student assignment"})
    reply.raise_for_status()
    path.write_bytes(reply.content)
    print(f"Saved data/{path.name} ({path.stat().st_size:,} bytes). Commit this file.")
    return path


if __name__ == "__main__":
    fetch(URL, DATA / FILE)
