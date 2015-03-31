import unittest
from props import config
from summoner_api_client import SummonerAPIClient

class SummonerAPIClientTest(unittest.TestCase):
  """Test for Summoner API Client"""

  def setUp(self):
    """Init client for test"""
    self.client = SummonerAPIClient('oce', config.lol_api_key)

  def test_byName(self):
    """Test fetch by summoner name"""
    self.client.byName("Minicat")


if __name__ == '__main__':
      unittest.main()
