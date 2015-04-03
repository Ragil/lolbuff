import webapp2
import logging
from api.lol.cached_client.match_history_api_client import MatchHistoryAPIClient
from api.lol.cached_client.summoner_api_client import SummonerAPIClient
from data.analyzer.trend import SummonerTrends
from base_request_handler import BaseRequestHandler


class TrendResponse(object):
  """Response for trend request"""

  def __init__(self):
    self.trend = None # Trend
    self.prefetching = False

  def as_dict(self):
    res = { 'prefetching' : self.prefetching }
    if self.trend:
      res['trend'] = self.trend.as_dict()

    return res


class Handler(BaseRequestHandler):
  """Handles trends statistics"""

  def __init__(self, request, response):
    """Initialize league api clients"""
    super(Handler, self).__init__(request, response)

    self._match_history_clients = dict(
        (region, MatchHistoryAPIClient(region,
            self.config.lol_api_key)) for region in self._regions )
    self._summoner_api_clients = dict(
        (region, SummonerAPIClient(region,
            self.config.lol_api_key)) for region in self._regions )

  @BaseRequestHandler.ensure_param('region')
  @BaseRequestHandler.ensure_param('summoner_name')
  @BaseRequestHandler.ensure_param('metric')
  def get(self, *args, **kwargs):
    """Return trend for requested filters"""
    params = self.request.GET
    region = params['region']
    summoner_name = params['summoner_name']
    metric = params['metric']

    if not self.has_valid_region():
      return

    if metric not in SummonerTrends.allowed_metrics:
      self.bad_request('Metric "%s" not supported. Supported metrics : %s' %
          (metric, SummonerTrends.allowed_metrics))
      return

    summoner = self._summoner_api_clients[region].by_name(summoner_name)
    if not summoner:
      self.bad_request('Summoner "%s" not found.')
      return

    match_history = self._match_history_clients[region].by_summoner_id(
        summoner.id, 0, 200)

    response_data = TrendResponse()
    response_data.trend = SummonerTrends(match_history, summoner.id).get(metric)
    self.respond_as_json(response_data.as_dict(), 200)
