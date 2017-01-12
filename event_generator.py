import json
import common.utils

new_event_data = {
    "derp": "kek"
}


if new_event_data:
    event_file = open(common.utils.event_source_file, "w")

    event_file.write(json.dumps(new_event_data))

    event_file.close()