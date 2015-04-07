import urllib
import logging
import time
from league_api_client import LeagueAPIClient
from api.lol.models import MatchHistory
from google.appengine.api import urlfetch

class MatchHistoryAPIClient(LeagueAPIClient):
  """API client for match history endpoint

  Refer to https://developer.riotgames.com/api/methods#!/978/3338 for more info
  """

  def __init__(self, region, api_key):
    """Create match history client

    region -- string :
        matchhistory-v2.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    api_key -- string : league api key
    """
    super(MatchHistoryAPIClient, self).__init__(region, api_key)
    self.baseURL = "https://%s.api.pvp.net/api/lol/%s/v2.2/matchhistory" % (region,
        region)

  def by_summoner_id(self, summoner_id, start_index=0, end_index=10):
    """Fetch match history for a summoner

    summoner_id -- string : league summonner id
    start_index -- int
    end_index -- int
    """
    payload = self.base_request_payload.copy()
    match_history = MatchHistory()

    # the api only allows a window of 10 games at a time
    for start in xrange(start_index, end_index, 10):
      payload.update({
        "beginIndex" : start,
        "endIndex" : min(end_index, start + 10)
      })

      # we retry three times with exponential back off
      # to account for cases where we get rate limited
      response = None
      attempt = 0
      while not response:
        attempt += 1
        response = urlfetch.fetch("%s/%s?%s" % (self.baseURL, summoner_id,
            urllib.urlencode(payload)))

        # fail to make request
        if response.status_code >= 300:
          if attempt >= 3:
            raise RuntimeError(response.content)

          # wait a bit
          delay = pow(2.0, attempt - 1) / 2
          logging.warning('Retrying request with delay %s because %s' %
              (delay, response.content))
          time.sleep(delay)
          response = None


      new_history = MatchHistory(response.content)

      # no more data, break early
      if not new_history.matches:
        return match_history

      match_history.update(new_history)

    return match_history

