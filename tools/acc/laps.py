from pathlib import Path
import json
import statistics
import sys

import pyperclip

practice1 = Path.home() / "Documents/Assetto Corsa Competizione/Results/Practice_1.json"
assert practice1.exists()

practice2 = Path.home() / "Documents/Assetto Corsa Competizione/Results/Practice_2.json"
assert practice2.exists()

latest = max(practice1, practice2, key=lambda p: p.stat().st_mtime)

print(f"Reading {latest}")
data = json.loads(latest.read_text("utf_16_le"))

laps = [l for l in data["laps"] if l["carId"] == 0]
fuel_used = []

print("\nLap       Time   Fuel")
for i, l in enumerate(laps, 0):
    if i == 0:
        print(f"{i+1:<4}{l["lapTime"]/1000:10}")
    else:
        fuel = laps[i-1]["fuel"] - l["fuel"]
        fuel_used.append(fuel)
        print(f"{i+1:<4}{l["lapTime"]/1000:10}\t{fuel:5.1f}")
print(f"\nAverage fuel per lap: {statistics.mean(fuel_used):.1f}")

lap_times = "\n".join(str(l["lapTime"]/1000) for l in laps)
pyperclip.copy(lap_times)
print("\nLap times copied to clipboard")
