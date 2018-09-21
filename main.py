import nhl
import json

def run():
    sched = nhl.fetch_schedule()
    with open("logs/test.json", "w") as logfile:
        logfile.write(json.dumps(sched, indent=4))

if __name__ == "__main__":
    run()
