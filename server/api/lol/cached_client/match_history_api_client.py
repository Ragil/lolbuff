import zlib

from google.appengine.ext import db
from api.lol.raw_client.match_history_api_client import (
    MatchHistoryAPIClient as RawClient
)

class CachedMatchHistory(db.Model):
  pass


class MatchHistoryAPIClient(object):
  """Match history api client with data caching to datastore and memcache"""

  def __init__(self, region, api_key):
    """Create match history client

    region -- string :
        matchhistory-v2.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    api_key -- string : league api key
    """
    self.raw_client = RawClient(region, api_key)

  def by_summoner_id(self, summoner_id, start_index=0, end_index=10):
    """Fetch match history for a summoner

    summoner_id -- string : league summonner id
    start_index -- int
    end_index -- int
    """
    return self.raw_client.by_summoner_id(summoner_id, start_index, end_index)

  def require_prefetch(self, summoner_id):
    """Returns True if the value requires prefetching"""
    return False
