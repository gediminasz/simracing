from dataclasses import dataclass
from enum import Enum


class Tyre(Enum):
    RS = 0
    RM = 1
    RH = 2


@dataclass
class RaceParameters:
    available_compounds: set
    required_compounds: set
    lap_count: int
    max_stint_length: int
    pit_cost: float
