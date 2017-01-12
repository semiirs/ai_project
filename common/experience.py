import datetime
import json


class Experience:

    def __init__(self, date, event):
        self._date = date
        self._event = event

    @classmethod
    def reconstruct_from_db_data_event(cls, date, event):
        event = json.loads(event)
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        exp = Experience(date, event)
        return exp

    def time_from_this_event(self, event):
        return self._date - event._date