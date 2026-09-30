# Process

This is an AI-assisted working draft, not a record of actions the student has already taken. Codex drafted the scripts and these notes. Before submission, I need to run the code, inspect the picture, and replace or confirm the decisions below in my own words. I should record any actual mistake and correction; I should not claim a review or correction I did not make.

## Tools

ChatGPT (Codex) helped draft the Python fetch and plotting scripts and the first README draft. The data source is the Hong Kong Observatory CSV listed on DATA.GOV.HK. The plot uses Python's built-in `csv` and `datetime` modules plus Matplotlib.

## Kept

The draft keeps the Observatory's CSV as the data file instead of editing it into a hand-made table. It uses one bar per date so individual wet days remain visible, and it labels the trace convention rather than pretending a trace is an exact measurement. Before submission, I need to run the scripts, inspect the resulting figure, and write down any corrections I actually make.

## Rejected

I rejected a monthly-total-only picture for this question because summing a month would hide which individual days produced the rainfall. I also rejected converting `Trace` to a made-up decimal amount; the chart shows traces separately at the baseline instead. These are the current draft decisions. I will revise this file if my review leads to different choices, and I will describe the actual corrections rather than claim work I did not do.
