import datetime
import os
import time
import sys

experience = dict()
experience["2017-01-12 19:20:40.674936"] = "i was born"


event_source_file = "new_event.txt"


def add_experience(event):
    this_file = open(__file__, "r")

    lines = this_file.readlines()
    for k, line in enumerate(lines):
        if line.startswith("experience"):
            lines.insert(k+1, 'experience["{0}"] = "{1}"\n'.format(datetime.datetime.now(), event))
            break

    this_file.close()

    this_file = open(__file__, "w")
    this_file.writelines(lines)
    this_file.close()


def learn():
    pass


def watch_world():
    try:
        event_file = open(event_source_file, "r")
    except:
        pass
    else:
        event = event_file.read()
        event_file.close()

        if event:
            print("Something happened in the world: " + event)
            add_experience(event)
            os.remove(event_source_file)

watch_world()

time.sleep(0.5)
print("Re-running self...")
python = sys.executable
os.execl(python, python, *sys.argv)