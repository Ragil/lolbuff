from lib.requests import api as requests
from league_api_client import LeagueAPIClient
from models import MatchHistory

class MatchHistoryAPIClient(LeagueAPIClient):
  """API client for match history endpoint

  Refer to https://developer.riotgames.com/api/methods#!/978/3338 for more info
  """

  def __init__(self, region, api_key=None):
    """Create match history client

    region -- string :
        matchhistory-v2.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    api_key -- string : league api key
    """
    super(MatchHistoryAPIClient, self).__init__(region, api_key)
    self.baseURL = "https://%s.api.pvp.net/api/lol/%s/v2.2/matchhistory" % (region,
        region)

  def by_summoner(self, summoner_id, start_index=0, end_index=10):
    """Fetch match history for a summoner

    summoner_id -- string : league summonner id
    """
    payload = self.base_request_payload.copy()
    match_history = MatchHistory()

    # the api only allows a window of 10 games at a time
    for end in xrange(start_index, end_index, 10):

      payload.update({
        "beginIndex" : start_index,
        "endIndex" : min(end_index, end)
      })

      response = requests.get("%s/%s" % (self.baseURL, summoner_id),
          params = self.base_request_payload)

      # fail to make request
      if response.status_code >= 300:
        raise RuntimeError(response.json())

      new_history = MatchHistory(response.text)

      # no more data, break early
      if not new_history.matches:
        return match_history

      match_history.update(new_history)

    return match_history

