from utilities import *

class Event:
    def __init__(self, _type, date, time, description):
        self._type = _type
        self.date = date
        self.time = convert_time(time) + " Eastern Standard Time (EST/EDT)"
        if description is None:
            self.description = "No description available at this time."
        else:
            self.description = " ".join(description)
        self.attendees = []

    def __repr__(self):
        return f"\n> **Type**:\n > {self._type}\n > **Date**:\n > {self.date}\n > **Time**:\n > {self.time}\n > **Description**:\n > {self.description}\n"
        