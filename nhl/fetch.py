from .urls import url_schedule
import requests

STARS_ID = 25

def fetch_schedule(team_id = STARS_ID):
    """ fetch the team's schedule for the day. team_id optional param, default to stars """

    url = url_schedule(team_id)

    # fetch, validate, and parse json
    req = requests.get(url)
    req.raise_for_status()
    return req.json()
