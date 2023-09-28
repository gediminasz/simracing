# Usage:
# poetry run python .\tools\printgt7laps.py

import os
import sys
import pathlib
import statistics

from gt7dashboard.gt7helper import load_laps_from_pickle
import pyperclip

repository_location = pathlib.Path("../gt7dashboard")
data_files = list((repository_location / "data").iterdir())
latest_file = sorted(data_files)[-1]
print(latest_file)

laps = load_laps_from_pickle(latest_file)
laps = list(reversed(laps))

mean_fuel = statistics.mean(l.fuel_consumed for l in laps[1:])

for l in laps:
    print(f"{l.number}\t{l.lap_finish_time/1000}")
print()
print(f"Avarage fuel per lap: {mean_fuel:.1f}")

lap_times = "\n".join(str(l.lap_finish_time/1000) for l in laps)
pyperclip.copy(lap_times)
print("Lap times copied to clipboard")
