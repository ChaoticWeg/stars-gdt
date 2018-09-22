from .urls import url_schedule
from datetime import datetime
import requests

STARS_ID = 25

def fetch_schedule(start_date, end_date, team_id = STARS_ID):
    """ fetch the team's schedule for the day. team_id optional param, default to stars """

    url = url_schedule(team_id, start_date, end_date)

    # fetch, validate, and parse json
    req = requests.get(url)
    req.raise_for_status()
    return req.json()
