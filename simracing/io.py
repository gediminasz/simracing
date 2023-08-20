import csv
from io import StringIO


def parse_lap_times(tsv_input):
    lap_times = {"RS": [], "RM": [], "RH": []}
    for line in csv.DictReader(StringIO(tsv_input.strip()), delimiter="\t"):
        for compound in lap_times.keys():
            if time := line.get(compound):
                lap_times[compound].append((int(line["Lap"]), float(time)))
    return lap_times
