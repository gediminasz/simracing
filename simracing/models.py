import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from simracing.constants import Tyre
from simracing.io import parse_lap_times


def fit_model(tsv_data, **kwargs):
    lap_time_data = parse_lap_times(tsv_data)

    tyre_models = {
        compound: _fit_linear_model(lap_times)
        for compound, lap_times in lap_time_data.items()
        if lap_times
    }

    for compound, model in tyre_models.items():
        colors = {Tyre.RS: "crimson", Tyre.RM: "orange", Tyre.RH: "dimgray"}
        _plot_model(
            lap_time_data[compound], model, kwargs["max_stint_length"], colors[compound]
        )

    return StrategyModel(tyre_models=tyre_models, **kwargs)


class StrategyModel:
    def __init__(
        self,
        *,
        tyre_models: dict,
        required_compounds: set,
        max_stint_length: int,
        pit_cost: float,
    ):
        self.tyre_models = tyre_models
        self.max_stint_length = max_stint_length
        self.required_compounds = required_compounds
        self.pit_cost = pit_cost

    def evaluate(self, stints):
        if stints[0][0] == -1:  # must start on some tyres
            return float("inf")

        if any(stint_length > self.max_stint_length for _, stint_length in stints):
            return float("inf")

        used_compounds = set(Tyre(s[0]) for s in stints)
        if used_compounds & self.required_compounds != self.required_compounds:
            return float("inf")

        time = 0
        for compound, stint_length in stints:
            x = [[i] for i in range(stint_length)]
            stint_time = sum(self.tyre_models[Tyre(compound)].predict(x))
            time += stint_time

        time += (len(stints) - 1) * self.pit_cost

        return time


def _fit_linear_model(lap_data):
    lap_numbers = [[x] for x, _ in lap_data]
    lap_times = [y for _, y in lap_data]
    return LinearRegression().fit(lap_numbers, lap_times)


def _plot_model(lap_times, model, xlimit, color):
    plt.scatter(
        [[x] for x, _ in lap_times], [y for _, y in lap_times], marker="x", color=color
    )

    x = [[i] for i in range(1, xlimit + 1)]
    y = model.predict(x)
    plt.plot(x, y, color=color, linewidth=3)

    plt.xlabel("Lap")
    plt.ylabel("Time")
