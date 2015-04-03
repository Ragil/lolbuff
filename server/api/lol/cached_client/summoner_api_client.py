from api.lol.raw_client import SummonerAPIClient as RawClient

class SummonerAPIClient(object):
  """Wrapper around raw client to provide caching"""

  def __init__(self, region, api_key=None):
    """Init cached client

    region -- string : summoner-v1.4 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    api_key -- string : league api key
    """
    self._raw_client = RawClient(region, api_key)

  def by_name(self, name):
    """Fetch summoner by name

    name -- string : summoner name

    return -- Summoner : a summoner object
    """
    return self._raw_client.by_name(name)
