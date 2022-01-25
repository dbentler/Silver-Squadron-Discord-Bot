"""
Helper functions for grabbing secret keys.
"""
from sys import platform
from datetime import datetime
from pathlib import Path

def get_project_root() -> Path:
    """
    Returns project root.
    """
    return Path(__file__).parent.parent

def refine_path() -> str:
    if platform == "linux" or platform == "linux2":
        return str(get_project_root()) + "/bot/"
    elif platform == "win32":
        return str(get_project_root()) + "\\bot\\"


def get_secrets(file_name: str) -> list:
    """
    Returns a lst of secret keys:
    [<discord secret>, <google sheets secret>]

    This way, we can store all of our secrets in one txt file, and grab them at inititalization.
    """
    text = ""
    secrets = []

    with open (refine_path() + file_name) as f:
        text = f.read()
        text.strip("\n")
        secrets.append(text)
    f.close()

    return secrets

def convert_time(time: str) -> str:
    divider = time.find(":")
    hour = int(time[:divider])

    if hour > 12:
        hour -= 12
        time += "pm"
    
    if (hour < 12) and (time.find("am") == -1):
        if time.find("pm") != -1:
            pass
        else:
            time += "am"
    
    converted = str(hour) + time[divider:]
    return converted

def date() -> str:
    now = datetime.now()

    dt_string = now.strftime("%m-%d-%Y_%H-%M-%S")
    return dt_string

def log(e: str) -> None:
    new_log = date() + ".txt"
    if platform == "win32":
        f = open(refine_path() + "logs\\" + new_log, "w+")
    if platform == "linux" or platform == "linux2":
        f = open(refine_path() + "logs/" + new_log, "w+")
    f.write(e)
    f.close()

def hour_out(timeA: str, timeB: str) -> bool:
    divider = timeA.find(":")
    hoursA = int(timeA[:divider])
    hoursB = int(timeB[:divider])

    if hoursB == (hoursA - 1):
        return True
    return False

def mil_to_civ(date: str) -> str:
    # This functions only works with $op, and follows strict typing.
    # It expects a date such as "29MAY21 2200"
    MONTH = {"JAN": "01", "FEB": "02", "MAR": "03",
             "APR": "04", "MAY": "05", "JUN": "06",
             "JUL": "07", "AUG": "08", "SEP": "09",
             "OCT": "10", "NOV": "11", "DEC": "12"}

    _month = MONTH[date[2:5]]
    year = str(int(date[5:]) + 2000)
    day = date[:2]
    
    return f"{_month}/{day}/{year}"

def mt_to_ct(time_t: str) -> str:
    # Converts military time with no special characters to 12 hour time.
    hours = time_t[:2]
    minutes = time_t[2:]
    civ_time = convert_time(hours + ":" + minutes)
    return civ_time
        

if __name__ == "__main__":
    # Debugging specific functions. These commands won't be run unless you run this specific file.
    _date = mil_to_civ("29MAY21")
    mt_to_ct("0000")