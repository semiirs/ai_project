import datetime
import os
import time
import sys
import common.utils
import sqlite3

# conn = sqlite3.connect('prod_events.db')
conn = sqlite3.connect('events.db')
c = conn.cursor()


def add_experience(event):
    event = [(str(datetime.datetime.now()), str(event))]
    c.executemany('INSERT INTO experiences (date, event) VALUES (?,?)', event)
    conn.commit()


def learn():
    for row in c.execute('SELECT * FROM experiences ORDER BY date'):
        print(row)


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

watch_world()
learn()

conn.close()
time.sleep(0.5)
print("Re-running self...")
python = sys.executable
os.execl(python, python, *sys.argv)