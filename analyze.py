import nhl

def run():
    sched = nhl.fetch_schedule()

    if sched["totalGames"] < 1:
        print("looks like there aren't any games today! bailing out.")
        return

    print("wake up! stars game day!")
    # TODO yeah

if __name__ == "__main__":
    run()

