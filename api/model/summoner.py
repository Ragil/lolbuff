import json

class Summoner:
  """Holds data about a summoner"""

  def __init__(self, raw_data_str):
    """Initialize a summoner based on raw response data

    raw_data_str -- string json response from summoner api request
    """

    self.data = json.loads(raw_data_str)
    self.data = self.data[self.data.keys()[0]]
    self.id = self.data.id
    self.name = self.data.name
    self.profileIconId = self.profileIconId
    self.revisionDate = self.revisionDate
    self.summonerLevel = self.summonerLevel

