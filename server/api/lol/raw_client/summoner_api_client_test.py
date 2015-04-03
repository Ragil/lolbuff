import unittest
import props
from google.appengine.ext import testbed
from summoner_api_client import SummonerAPIClient

class SummonerAPIClientTest(unittest.TestCase):
  """Test for Summoner API Client"""

  def setUp(self):
    """Init client for test"""
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_urlfetch_stub()
    self.client = SummonerAPIClient("oce", props.get_config().lol_api_key)

  def tearDown(self):
    self.testbed.deactivate()

  def test_by_name(self):
    """Test fetch by summoner name"""
    summoner = self.client.by_name("Minicat")
    self.assertEquals(summoner.name, "Minicat")
    self.assertEquals(summoner.summonerLevel, 30)


if __name__ == '__main__':
  unittest.main()
