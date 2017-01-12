import datetime
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


def add_experience(event):
    event = [(str(datetime.datetime.now()), str(event))]
    c.executemany('INSERT INTO experiences (date, event) VALUES (?,?)', event)
    conn.commit()


def learn():

    for row in c.execute('SELECT * FROM experiences ORDER BY date DESC'):
        common.code_manipulation.add_code_line_at_start(str(row[0]))


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