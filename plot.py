# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///
"""Plot the Observatory's daily rainfall record.

    uv run plot.py
"""

import csv
from datetime import date, timedelta
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

FILE = "daily_HKO_RF_2026.csv"
PICTURE = "plot.png"
HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"


def read_observations(path: Path) -> list[tuple[date, float, bool]]:
    """Return (date, rainfall_mm, is_trace) records from the HKO CSV."""
    observations = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.reader(handle):
            if not row or not row[0].isdigit():
                continue
            year, month, day = (int(part) for part in row[:3])
            raw_value = row[3].strip()
            if raw_value == "***":
                continue
            is_trace = raw_value.lower() == "trace"
            amount = 0.0 if is_trace else float(raw_value)
            observations.append((date(year, month, day), amount, is_trace))
    return observations


def main() -> None:
    observations = read_observations(DATA)
    if not observations:
        raise ValueError(f"No daily observations found in {DATA}")

    dates = [item[0] for item in observations]
    rainfall = [item[1] for item in observations]
    trace_dates = [item[0] for item in observations if item[2]]
    peak_index = max(range(len(rainfall)), key=rainfall.__getitem__)
    peak_date, peak_mm = dates[peak_index], rainfall[peak_index]
    print(f"{DATA.name}: {len(observations)} dated records through {dates[-1]}.")
    print(f"Peak recorded rainfall: {peak_mm:g} mm on {peak_date.day} {peak_date:%b}.")
    print(f"Trace-only days shown as zero-height bars: {len(trace_dates)}.")

    fig, ax = plt.subplots(figsize=(12, 5.5), facecolor="#f7fafc")
    ax.set_facecolor("#f7fafc")
    ax.bar(dates, rainfall, width=0.85, color="#168aad", edgecolor="none", zorder=3)
    if trace_dates:
        ax.scatter(trace_dates, [0.6] * len(trace_dates), marker="|", s=44,
                   linewidths=1.2, color="#6c8293", label="Trace (<0.05 mm)", zorder=4)
        ax.legend(frameon=False, loc="upper left")

    ax.annotate(f"{peak_mm:g} mm\n{peak_date.day} {peak_date:%b}",
                xy=(peak_date, peak_mm), xytext=(10, 10), textcoords="offset points",
                fontsize=9, color="#123047", fontweight="bold",
                arrowprops={"arrowstyle": "-", "color": "#526b7a", "lw": 0.8})
    ax.set_title("Hong Kong rain comes in bursts", loc="left", pad=18,
                 fontsize=18, fontweight="bold", color="#123047")
    ax.text(0, 1.02,
            f"Daily total at the Hong Kong Observatory · 2026 through {dates[-1]:%d %b} · peak {peak_mm:g} mm",
            transform=ax.transAxes, fontsize=9.5, color="#526b7a")
    ax.set_ylabel("Daily rainfall (mm)", color="#344c5c")
    ax.set_xlabel("2026", color="#344c5c", labelpad=10)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
    ax.set_xlim(date(dates[0].year, 1, 1), dates[-1] + timedelta(days=2))
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", color="#dbe5eb", linewidth=0.8, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color("#b7c7d1")
    ax.tick_params(axis="both", colors="#526b7a", length=0, pad=7)
    fig.text(0.01, 0.015,
             "Source: Hong Kong Observatory · Trace means less than 0.05 mm; plotted at zero.",
             fontsize=8, color="#637989")
    fig.tight_layout(rect=(0, 0.04, 1, 0.97))

    OUT.mkdir(exist_ok=True)
    destination = OUT / PICTURE
    fig.savefig(destination, dpi=180, facecolor=fig.get_facecolor())
    print(f"Saved out/{PICTURE}")
    plt.show()


if __name__ == "__main__":
    main()
