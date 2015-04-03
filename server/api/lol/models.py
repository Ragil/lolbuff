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
    data = json.loads(raw_data)
    data = data[data.keys()[0]]

    for k, v in data.items():
      setattr(self, k, v)


class ParticipantStats(object):
  """Holds participant stats"""

  def __init__(self, data):
    """Init stats from parsed data"""
    for k, v in data.items():
      setattr(self, k, v)


class Player(object):
  """A crappy representation of Summoner when in the context of a Match Summary"""

  def __init__(self, data):
    """Init player from parsed data"""
    for k, v in data.items():
      setattr(self, k, v)


class ParticipantIdentity(object):
  """Holds participant identity"""

  def __init__(self, data):
    """Init participant identity from parsed data"""
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
    for k, v in data.items():
      setattr(self, k, v)

    self.stats = ParticipantStats(self.stats)


class MatchSummary(object):
  """Holds summary data about a match

  Refer to https://developer.riotgames.com/api/methods#!/978/3338 for more info.
  """

  def __init__(self, data):
    """Init match summary from parsed data"""
    for k, v in data.items():
      setattr(self, k, v)

    self.participantIdentities = [
        ParticipantIdentity(i) for i in self.participantIdentities ]
    self.participants = [ Participant(p) for p in self.participants ]

  def participant_by_summoner_id(self, summoner_id):
    """Return participant id for a given summoner id

    summoner_id -- string : a summoner id
    return particiant id or None
    """
    for participant_identity in self.participantIdentities:
      if participant_identity.player.summonerId == summoner_id:
        return self.participant_by_id(participant_identity.participantId)

    return None

  def participant_by_id(self, participant_id):
    """Returns the participant that match the given id

    participant_id -- int : ParticipantIdentity.participantId
    return participant or None
    """
    for participant in self.participants:
      if participant.participantId == participant_id:
        return participant
    return None

  @property
  def epoch_day(self):
    """Return the match day in epoch"""
    return self.matchCreation - (self.matchCreation % 86400000)

  def __eq__(self, other):
    return self.matchId == other.matchId

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
    self.matches = []

    if raw_data:
      data = json.loads(raw_data)
      self.matches = [
          MatchSummary(summary_data) for summary_data in data["matches"] ]

  def update(self, other_history):
    """Modify the current history with data from other history

    other_history -- MatchHistory : other history for the same summoner
    """
    unique_matches = set(self.matches)
    unique_matches = unique_matches.union(other_history.matches)
    self.matches = list(unique_matches)
    self.matches.sort(key=lambda x: x.matchCreation, reverse=True)


