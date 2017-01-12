import datetime
import common.experience
import os
import time
import sys
import common.utils
import common.code_manipulation

import sqlite3

# conn = sqlite3.connect('prod_events.db')
conn = sqlite3.connect('events.db')
c = conn.cursor()

effect_fade_seconds = 3

event_frequency_threshold = 2
event_intensity_time_threshold = 3


def check_event_frequency(event, period_since_now):
    events = []
    number_of_events_in_period = 0
    now = datetime.datetime.now()

    for row in c.execute('SELECT date, event FROM experiences WHERE event LIKE \'' + event + '\' ORDER BY date DESC'):
        exp = common.experience.Experience.reconstruct_from_db_data_event(row[0], row[1])
        events.append(exp)

    for event in events:
        if now - event._date < period_since_now:
            number_of_events_in_period += 1

    return number_of_events_in_period


def add_experience(event):
    event = [(str(datetime.datetime.now()), str(event))]
    c.executemany('INSERT INTO experiences (date, event) VALUES (?,?)', event)
    conn.commit()


def learn():
    pass


def handle_immediate_experience(event):
    interval = datetime.timedelta(minutes=2)
    times = check_event_frequency(event, interval)

    print("This event has happened {0} times in the last 2 minutes.".format(times))
    if times > event_frequency_threshold:
        pass


def apply_knowledge():
    return


def watch_world():
    try:
        event_file = open(common.utils.event_source_file, "r")
    except:
        pass
    else:
        event = event_file.read()
        event_file.close()

        if event:
            print("Something happened in the world: " + event)
            handle_immediate_experience(event)
            add_experience(event)
            os.remove(common.utils.event_source_file)

this_file = open(__file__, "r")
lines = this_file.readlines()
this_file.close()
common.code_manipulation.set_content(lines)

watch_world()
learn()
apply_knowledge()

if common.code_manipulation.was_any_code_modified():
    this_file = open(__file__, "w")
    lines = common.code_manipulation.get_content()
    this_file.writelines(lines)
    this_file.close()

conn.close()
time.sleep(0.5)
print("Re-running self...")
python = sys.executable
os.execl(python, python, *sys.argv)