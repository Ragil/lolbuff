from league_api_client import LeagueAPIClient
from lib.requests import api as requests

class SummonerAPIClient(LeagueAPIClient):
  """Client API for Summoner endpoint

  Refer to https://developer.riotgames.com/api/methods#!/960 for more info.
  """

  def __init__(self, region, api_key):
    """Create a client API for a particular region

    region -- string : summoner-v1.4 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    """
    super(SummonerAPIClient, self).__init__(region, api_key)
    self.baseURL = "https://%s.api.pvp.net/api/lol/%s/v1.4/summoner" % (region,
        region)
    self.byNameURL = "%s/by-name" % (self.baseURL)

  def byName(self, name):
    """Fetch summoner by name

    name -- string : summoner name
    """
    response = requests.get("%s/%s" % (self.byNameURL, name),
        params=self.baseRequestPayload)
    print(response.json())
