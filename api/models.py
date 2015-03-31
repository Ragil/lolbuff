import json
import sys

class Summoner(object):
  """Holds data about a summoner

  Refer to https://developer.riotgames.com/api/methods#!/960/3292 for more info.
  """

  def __init__(self, raw_data):
    """Initialize a summoner based on raw response data

    raw_data -- string : json response from summoner api request
    """
    self.data = json.loads(raw_data)
    self.data = self.data[self.data.keys()[0]]

    for k, v in self.data.items():
      setattr(self, k, v)


class Player(object):
  """A crappy representation of Summoner when in the context of a Match Summary"""

  def __init__(self, data):
    """Init player from parsed data"""
    self.data = data
    for k, v in data.items():
      setattr(self, k, v)


class ParticipantIdentity(object):
  """Holds participant identity"""

  def __init__(self, data):
    """Init participant identity from parsed data"""
    self.data = data
    for k, v in data.items():
      setattr(self, k, v)

    self.player = Player(self.player)

  def __str__(self):
    """Return summonerId"""
    return str(self.player.summonerName)

  def __repr__(self):
    return self.__str__()


class Participant(object):
  """Holds participant"""

  def __init__(self, data):
    """Init participant from parsed data"""
    self.data = data
    for k, v in self.data.items():
      setattr(self, k, v)


class MatchSummary(object):
  """Holds summary data about a match

  Refer to https://developer.riotgames.com/api/methods#!/978/3338 for more info.
  """

  def __init__(self, data):
    """Init match summary from parsed data"""
    self.data = data
    for k, v in self.data.items():
      setattr(self, k, v)

    self.participantIdentities = [
        ParticipantIdentity(i) for i in self.participantIdentities ]
    self.participants = [ Participant(p) for p in self.participants ]

  def __hash__(self):
    """Return the match id for the summary"""
    return self.matchId

  def __repr__(self):
    return str(self.matchId)


class Match(MatchSummary):
  """ Holds information about a match

  https://developer.riotgames.com/api/methods#!/967/3313
  """


class MatchHistory(object):
  """Holds player match history

  Refer to https://developer.riotgames.com/api/methods#!/978/3338 for more info.
  """

  def __init__(self, raw_data=None):
    """Init player history based on raw response data

    raw_data -- string : json response from match history api request
    """
    self.data = { "matches" : [] }
    self.matches = []

    if raw_data:
      self.data = json.loads(raw_data)
      self.matches = [
          MatchSummary(summary_data) for summary_data in self.data["matches"] ]

  def update(self, other_history):
    """Modify the current history with data from other history

    other_history -- MatchHistory : other history for the same summoner
    """
    unique_matches = set(self.matches)
    unique_matches = unique_matches.union(other_history.matches)
    self.matches = list(unique_matches)
    self.matches.sort(key=lambda x: x.matchCreation, reverse=True)


