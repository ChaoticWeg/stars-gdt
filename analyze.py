import nhl
from datetime import datetime, timedelta
from dateutil import parser as dt_parser
from dateutil import tz     as dt_tz

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

    # ZULU TIME
    next_game_date = min([ dt_parser.parse(game["gameDate"]) for game in upcoming_games ])
    with open("logs/next_game_date.txt", "w") as outfile:
        outfile.write(str(next_game_date))

if __name__ == "__main__":
    run()
