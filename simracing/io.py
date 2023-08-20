import csv
from io import StringIO

from simracing.constants import Tyre


def parse_lap_times(tsv_input):
    result = {Tyre.RS: [], Tyre.RM: [], Tyre.RH: []}
    lines = csv.DictReader(StringIO(tsv_input.strip()), delimiter="\t")
    for line in lines:
        for compound in result.keys():
            if lap_time := line.get(compound.name):
                result[compound].append((int(line["Lap"]), float(lap_time)))
    return result


example1 = """
Lap	RS	RM
2	91.994	92.224
3	91.580	91.934
4		91.481
"""
assert parse_lap_times(example1) == {
    Tyre.RS: [(2, 91.994), (3, 91.580)],
    Tyre.RM: [(2, 92.224), (3, 91.934), (4, 91.481)],
    Tyre.RH: [],
}
