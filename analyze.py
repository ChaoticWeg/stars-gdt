import nhl
from datetime import datetime, timedelta


def run():
    start_date = datetime.utcnow() - timedelta(days=1)
    end_date   = datetime.utcnow() + timedelta(days=4)

    sched = nhl.fetch_schedule(start_date, end_date)

    if sched["totalGames"] < 1:
        print("looks like there aren't any games for a while! bailing out.")
        return
    
    relevant_dates = [ date["games"] for date in sched["dates"] if date["totalGames"] > 0 ]
    upcoming_games = [ game["gameDate"] for games in relevant_dates for game in games ]

    next_game_date = min([ datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ") for dt in upcoming_games ])
    print("next stars game day is " + next_game_date.strftime("%m-%d-%Y at %H:%M:%S"))


if __name__ == "__main__":
    run()
