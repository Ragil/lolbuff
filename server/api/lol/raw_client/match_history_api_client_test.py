import unittest
import sys
import props

from match_history_api_client import MatchHistoryAPIClient
from google.appengine.ext import testbed

class MatchHistoryAPIClientTest(unittest.TestCase):
  """Tests for match history api client"""

  def setUp(self):
    """Initialize test"""
    self.testbed = testbed.Testbed()
    self.testbed.activate()
    self.testbed.init_urlfetch_stub()
    self.client = MatchHistoryAPIClient("oce", props.get_config().lol_api_key)

  def tearDown(self):
    self.testbed.deactivate()

  def test_by_summoner_id(self):
    """Test fetching match history by summoner id"""
    history = self.client.by_summoner_id(469407, 0, 20)
    self.assertEquals(len(history.matches), 20)


if __name__ == '__main__':
      unittest.main()
