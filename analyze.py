import nhl
from datetime import datetime, timedelta

""" filter irrelevant dates out of the list """
filter_dates = lambda dates: [ date for date in dates if date["totalGames"] > 0 ]

""" flatten a list of schedule dates into their games """
flatten_dates = lambda dates: [ game for date in dates for game in date["games"] ]

def run():
    """ main executing function """

    start_date = datetime.utcnow() - timedelta(days=1)
    end_date   = datetime.utcnow() + timedelta(days=4)

    sched = nhl.fetch_schedule(start_date, end_date)

    if sched["totalGames"] < 1:
        print("looks like there aren't any games for a while! bailing out.")
        return
    
    all_dates      = sched["dates"]
    relevant_dates = filter_dates(all_dates)
    upcoming_games = flatten_dates(relevant_dates)

    # remember: this is UTC!
    next_game_date = min([ datetime.strptime(game["gameDate"], "%Y-%m-%dT%H:%M:%SZ") for game in upcoming_games ])
    print("Next Stars game is " + next_game_date.strftime("%m-%d-%Y at %H:%M:%S"))


if __name__ == "__main__":
    run()
