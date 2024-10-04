import json
import sys
from pathlib import Path
from string import Template

import fire

TRACKS = {t["name"]: t["id"] for t in json.loads(Path("enum/tracks.json").read_text())["response"]["list"]}

VEHICLE_CLASSES = {
    c["name"]: c["value"] for c in json.loads(Path("enum/vehicle_classes.json").read_text())["response"]["list"]
}


def generate_config(
    *,
    template_path: Path | str,
    output_path: Path | str,
    vehicle_class: str,
    track: str,
):
    template = Template(Path(template_path).read_text())
    output = template.substitute(
        track_id=TRACKS[track],
        vehicle_class=VEHICLE_CLASSES[vehicle_class],
    )
    Path(output_path).write_text(output)


if __name__ == "__main__":
    fire.Fire(generate_config)
