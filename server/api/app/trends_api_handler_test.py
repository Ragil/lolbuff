import unittest
import webapp2
import main
import json
import urllib
from mock import MagicMock
from google.appengine.ext import testbed
from trends_api_handler import Handler
from data.analyzer.trend import SummonerTrends
from api.lol.models import Summoner
from api.lol.models import MatchHistory
from api.lol.cached_client.summoner_api_client import SummonerAPIClient
from api.lol.cached_client.match_history_api_client import MatchHistoryAPIClient
from api.lol.sampledata import data as sampledata

class HandlerTest(unittest.TestCase):
  """Test for trends api Handler"""

  def setUp(self):
    """Init testbest"""
    self.testbed = testbed.Testbed()
    self.testbed.activate()

  def tearDown(self):
    """Clean up"""
    self.testbed.deactivate()

  def _test_get(self, data, expected_status_int, expected_body,
      match_history_api_clients=None, summoner_api_clients=None):
    """Helper to test get request with expected output"""
    self.request = webapp2.Request.blank("%s?%s" %
        ('/api/trends', urllib.urlencode(data)))
    self.response = webapp2.Response()

    self.handler = Handler(self.request, self.response,
        match_history_api_clients, summoner_api_clients)
    self.handler.get()

    self.assertEquals(expected_status_int, self.response.status_int)
    self.assertEquals(json.dumps(expected_body), self.response.body)

  def test_get_missing_region(self):
    """Ensure that region is provided"""
    self._test_get({}, 400, {
      'error_msg' : 'Missing parameter "region"'
    })

  def test_get_missing_summoner_name(self):
    """Ensure that summoner_name is provided"""
    self._test_get({
      'region' : 'oce'
    }, 400, {
      'error_msg' : 'Missing parameter "summoner_name"'
    })

  def test_get_missing_metric(self):
    """Ensure that metric is provided"""
    self._test_get({
      'region' : 'oce',
      'summoner_name' : 'name'
    }, 400, {
      'error_msg' : 'Missing parameter "metric"'
    })

  def test_get_invalid_region(self):
    """Ensure that provided region is a valid value"""
    self._test_get({
      'region' : 'invalid_region',
      'summoner_name' : 'name',
      'metric' : 'goldpm'
    }, 400, {
      'error_msg' : 'Invalid region "invalid_region". Valid regions : %s' %
          Handler.regions
    })

  def test_get_invalid_metric(self):
    """Ensure that provided metric is a valid value"""
    self._test_get({
      'region' : 'oce',
      'summoner_name' : 'name',
      'metric' : 'invalid_metric'
    }, 400, {
      'error_msg' : 'Invalid metric "invalid_metric". Valid metrics : %s' %
          SummonerTrends.allowed_metrics
    })

  def test_get_summoner_does_not_exist(self):
    """Ensure that summoner exist"""
    mock_client = MagicMock(SummonerAPIClient)
    mock_client.by_name.return_value = None

    self._test_get({
      'region' : 'oce',
      'summoner_name' : 'invalid_name',
      'metric' : 'goldpm'
    }, 400, {
      'error_msg' : 'Summoner "invalid_name" not found in region "oce"'
    }, summoner_api_clients = {
      'oce' : mock_client
    })

  def test_get_has_match_history(self):
    """A successful get request for summoner trends"""
    mock_summoner = Summoner(sampledata.raw_summoner)

    mock_summoner_client = MagicMock(SummonerAPIClient)
    mock_summoner_client.by_name.return_value = mock_summoner

    mock_history = MatchHistory(sampledata.raw_match_history)

    mock_match_client = MagicMock(MatchHistoryAPIClient)
    mock_match_client.by_summoner_id.return_value = mock_history
    mock_match_client.require_prefetch.return_value = False

    self._test_get({
      'region' : 'oce',
      'summoner_name' : 'invalid_name',
      'metric' : 'goldpm'
    }, 200, {
      "prefetching": False,
      "trend": {
        "data_day_cumulative": [
          [1425254400000, 353.73],
          [1425340800000, 343.41],
          [1426291200000, 322.87],
          [1426896000000, 317.68],
          [1427414400000, 318.33]
        ],
        "name": "GPM",
        "data_day": [
          [1425254400000, 353.73],
          [1425340800000, 333.08],
          [1426291200000, 302.33],
          [1426896000000, 276.19],
          [1427414400000, 324.18]
        ]
      }
    }, match_history_api_clients = {
      'oce' : mock_match_client
    }, summoner_api_clients = {
      'oce' : mock_summoner_client
    })

  def test_get_require_prefetching(self):
    """Test for match history that need prefetching"""
    mock_summoner = Summoner(sampledata.raw_summoner)

    mock_summoner_client = MagicMock(SummonerAPIClient)
    mock_summoner_client.by_name.return_value = mock_summoner

    mock_match_client = MagicMock(MatchHistoryAPIClient)
    mock_match_client.require_prefetch.return_value = True

    self._test_get({
      'region' : 'oce',
      'summoner_name' : 'invalid_name',
      'metric' : 'goldpm'
    }, 200, {
      "prefetching": True,
    }, match_history_api_clients = {
      'oce' : mock_match_client
    }, summoner_api_clients = {
      'oce' : mock_summoner_client
    })


if __name__ == "__main__":
  unittest.main()
