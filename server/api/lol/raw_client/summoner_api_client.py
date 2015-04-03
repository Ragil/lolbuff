import urllib
from league_api_client import LeagueAPIClient
from api.lol.models import Summoner
from google.appengine.api import urlfetch

class SummonerAPIClient(LeagueAPIClient):
  """Client API for Summoner endpoint

  Refer to https://developer.riotgames.com/api/methods#!/960 for more info.
  """

  def __init__(self, region, api_key):
    """Create a client API for a particular region

    region -- string : summoner-v1.4 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    api_key -- string : league api key
    """
    super(SummonerAPIClient, self).__init__(region, api_key)
    self.baseURL = "https://%s.api.pvp.net/api/lol/%s/v1.4/summoner" % (region,
        region)
    self.byNameURL = "%s/by-name" % (self.baseURL)

  def by_name(self, name):
    """Fetch summoner by name

    name -- string : summoner name

    return -- Summoner : a summoner object
    """
    response = urlfetch.fetch("%s/%s?%s" % (self.byNameURL, name,
        urllib.urlencode(self.base_request_payload)))
    if response.status_code < 300 and response.status_code >= 200:
      return Summoner(response.content)

    raise RuntimeError(response.content)

