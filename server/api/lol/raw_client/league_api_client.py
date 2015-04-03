class LeagueAPIClient(object):
  """Base class for all League API clients"""

  def __init__(self, region, api_key):
    """Initialize client for a given region

    region -- string : Refer to each specific client for a list of regions
    api_key -- string : league api key
    """
    self.region = region
    self.api_key = api_key
    self.base_request_payload = {
      'api_key' : self.api_key
    }
