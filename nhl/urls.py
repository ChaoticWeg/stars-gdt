from datetime import datetime

DT_FORMAT = "%Y-%m-%d"                      # datetime format
BASE_URL  = "https://statsapi.web.nhl.com"  # base API url

def url_schedule(team_id, start_date, end_date):
    """ Get the fully qualified API URL from which to grab team schedule """

    # dict: URL querystring params
    params = {
        "site": "en_nhl",
        "season": "20182019",
        "startDate": start_date.strftime(DT_FORMAT),
        "endDate": end_date.strftime(DT_FORMAT),
        "teamId": team_id,
        "hydrate": "team(leaders(categories=[points,goals,assists],gameTypes=[P])),linescore,broadcasts(all),tickets,game(content(media(epg),highlights(scoreboard)),seriesSummary),radioBroadcasts,metadata,decisions,scoringplays,seriesSummary(series)" # TODO oh god the horror
    }

    return with_query(from_href("/api/v1/schedule"), params)



def from_href(href):
    """ Get a fully qualified API URL given only the href """

    # TODO better way?
    return BASE_URL + href



def with_query(url, params):
    """ Add query string, e.g. <url>?param1=val1&param2=val2&...&paramN=valN """

    # add initial ?
    result = url + "?"

    # iterate over parameters, adding as query-string key/value pairs e.g. param1=val1&
    # TODO FIXME url-encode
    for key in params:
        result += key + "=" + str(params[key]) + "&"

    # strip trailing &
    return result[:-1]
