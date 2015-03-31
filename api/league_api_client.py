class LeagueAPIClient(object):
  """Base class for all League API clients"""

  def __init__(self, region, api_key):
    """Initialize client for a given region

    region -- Refer to each specific client for a list of regions
    """
    self.region = region
    self.api_key = api_key
    self.baseRequestPayload = {
      'api_key' : self.api_key
    }
