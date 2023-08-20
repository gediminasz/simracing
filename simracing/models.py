import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from simracing.constants import Tyre


def fit_linear_models(lap_time_data, max_stint_length):
    models = {
        compound: _fit_linear_model(lap_times)
        for compound, lap_times in lap_time_data.items()
        if lap_times
    }

    for compound, model in models.items():
        colors = {Tyre.RS: "crimson", Tyre.RM: "orange", Tyre.RH: "dimgray"}
        _plot_model(lap_time_data[compound], model, max_stint_length, colors[compound])

    return models


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
