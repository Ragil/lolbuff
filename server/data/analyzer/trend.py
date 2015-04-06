import collections

class Trend(object):
  """Holds trends for a given metric"""

  def __init__(self, name, match_history, filter_fn, mode='avg'):
    """Init trend

    name -- string : the metric name
    match_history -- MatchHistory : match history
    filter_fn -- function : filter function to extract metric
    mode -- str : ['avg', 'sum'] when multiple fall into the same bucket
    """
    self.name = name

    day_bucket = {}
    for match_summary in match_history.matches:
      if match_summary.epoch_day not in day_bucket:
        day_bucket[match_summary.epoch_day] = []

      day_bucket[match_summary.epoch_day].append(filter_fn(match_summary))

    total = 0.0
    n = 0
    self.data_day_cumulative = []
    self.data_day = []

    for k in sorted(day_bucket):
      v = day_bucket[k]

      total += sum(v)
      n += len(v)

      if mode == 'avg':
        self.data_day_cumulative.append((k, round(total / n, 2)))
        self.data_day.append((k, round(float(sum(v)) / len(v), 2)))

      if mode == 'sum':
        self.data_day_cumulative.append((k, round(total, 2)))
        self.data_day.append((k, round(float(sum(v)), 2) ))


  def __repr__(self):
    return str(self.data_all)

  def as_dict(self):
    """Returns dict representation for json serialization"""
    return {
      'name' : self.name,
      'data_day_cumulative' : self.data_day_cumulative,
      'data_day' : self.data_day
    }


class SummonerTrends(object):
  """Holds all trends for a given summoner"""

  allowed_metrics = ['goldpm', 'kda', 'winrate', 'games']

  def __init__(self, match_history, summoner_id):
    """Init empty Trends"""
    self._match_history = match_history
    self._summoner_id = summoner_id

    # FIXME - probably shouldn't precompute every trend at once, we will never
    #         request them all at the same time anyway.
    self._trends = {
      'goldpm' : Trend("GPM", match_history, self._gpm_fn),
      'kda' : Trend("KDA", match_history, self._kda_fn),
      'winrate' : Trend("Win Rate", match_history, self._winrate_fn),
      'games' : Trend('Games Played', match_history, lambda a: 1, 'sum')
    }

  def get(self, metric):
    """Return Trend for metric"""
    return self._trends[metric]

  def _gpm_fn(self, match_summary):
    """Returns gpm for the current summoner"""
    participant = match_summary.participant_by_summoner_id(self._summoner_id)
    return float(participant.stats.goldEarned) / match_summary.matchDuration * 60

  def _kda_fn(self, match_summary):
    """Returns kda for the current summoner"""
    participant = match_summary.participant_by_summoner_id(self._summoner_id)
    ka = participant.stats.kills + participant.stats.assists
    d = max(participant.stats.deaths, 1)
    return float(ka) / d

  def _winrate_fn(self, match_summary):
    """Returns winrate for the current summoner"""
    participant = match_summary.participant_by_summoner_id(self._summoner_id)
    return 1.0 if participant.stats.winner else 0.0
