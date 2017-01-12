import json
import common.utils


def create_event(data: dict):
    event_file = open(common.utils.event_source_file, "w")

    event_file.write(json.dumps(data))

    event_file.close()