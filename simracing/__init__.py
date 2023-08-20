from simracing.models import fit_model
from simracing.strategy import predict_strategy
from simracing.types import RaceParameters


def strategize(data: str, **kwargs):
    race_parameters = RaceParameters(**kwargs)

    model = fit_model(tsv_data=data, race_parameters=race_parameters)

    predict_strategy(model, race_parameters)

    return model
