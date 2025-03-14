import json
import sys
from datetime import datetime
from pathlib import Path
from string import Template

import fire

TRACKS = {t["name"]: t["id"] for t in json.loads(Path("enum/tracks.json").read_text())["response"]["list"]}

VEHICLE_CLASSES = {
    c["name"]: c["value"] for c in json.loads(Path("enum/vehicle_classes.json").read_text())["response"]["list"]
}

FLAGS = {f["name"]: f["value"] for f in json.loads(Path("enum/flags.json").read_text())["response"]["list"]}


def generate_config(
    *,
    template_path: Path | str,
    output_path: Path | str,
    vehicle_class: str,
    track: str,
):
    today = datetime.today()
    template = Template(Path(template_path).read_text())
    output = template.substitute(
        track_id=TRACKS[track],
        vehicle_class=VEHICLE_CLASSES[vehicle_class],
        flags=(
            FLAGS["ABS_ALLOWED"]
            + FLAGS["SC_ALLOWED"]
            + FLAGS["TCS_ALLOWED"]
            + FLAGS["FORCE_SAME_VEHICLE_CLASS"]
            + FLAGS["FILL_SESSION_WITH_AI"]
            + FLAGS["AUTO_START_ENGINE"]
            + FLAGS["TIMED_RACE"]
            + FLAGS["ONLINE_REPUTATION_ENABLED"]
            + FLAGS["WAIT_FOR_RACE_READY_INPUT"]
        ),
        race_date_year=today.year,
        race_date_month=today.month,
        race_date_day=today.day,
    )
    Path(output_path).write_text(output)


if __name__ == "__main__":
    fire.Fire(generate_config)
