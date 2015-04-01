import unittest

from match_history_api_client import MatchHistoryAPIClient

class MatchHistoryAPIClientTest(unittest.TestCase):
  """Tests for match history api client"""

  def setUp(self):
    """Initialize test"""
    self.client = MatchHistoryAPIClient("oce")

  def test_by_summoner(self):
    """Test fetching match history by summoner id"""
    history = self.client.by_summoner(469407, 0, 20)
    self.assertEquals(len(history.matches), 20)

if __name__ == '__main__':
      unittest.main()
