import unittest

from trend import SummonerTrends
from api.lol.sampledata import data
from api.lol.models import MatchHistory

class SummonerTrendsTest(unittest.TestCase):
  """Test for SummonerTrends"""

  def setUp(self):
    """Init test"""
    self.match_history = MatchHistory(data.raw_match_history)
    self.trend = SummonerTrends(self.match_history, 363043)
    self.assertEquals(10, len(self.match_history.matches))

  def test_gpm(self):
    """Extract daily gpm"""
    gpm_trend = self.trend.get('goldpm')
    data = gpm_trend.data_day
    self.assertEquals(5, len(data))
    self.assertEquals((1425254400000, 353.73), data[0])
    self.assertEquals((1425340800000, 333.08), data[1])
    self.assertEquals((1426291200000, 302.33), data[2])
    self.assertEquals((1426896000000, 276.19), data[3])
    self.assertEquals((1427414400000, 324.18), data[4])

  def test_gpm_comulative(self):
    """Extract day comulative gpm"""
    gpm_trend = self.trend.get('goldpm')
    data = gpm_trend.data_day_comulative
    self.assertEquals(5, len(data))
    self.assertEquals((1425254400000, 353.73), data[0])
    self.assertEquals((1425340800000, 343.41), data[1])
    self.assertEquals((1426291200000, 322.87), data[2])
    self.assertEquals((1426896000000, 317.68), data[3])
    self.assertEquals((1427414400000, 318.33), data[4])

  def test_kda(self):
    """Extract daily kda"""
    kda_trend = self.trend.get('kda')
    data = kda_trend.data_day
    self.assertEquals(5, len(data))
    self.assertEquals((1425254400000, 3.91), data[0])
    self.assertEquals((1425340800000, 1.44), data[1])
    self.assertEquals((1426291200000, 4.42), data[2])
    self.assertEquals((1426896000000, 0.5), data[3])
    self.assertEquals((1427414400000, 1.29), data[4])

  def test_kda_comulative(self):
    """Extract day comulative kda"""
    kda_trend = self.trend.get('kda')
    data = kda_trend.data_day_comulative
    self.assertEquals(5, len(data))
    self.assertEquals((1425254400000, 3.91), data[0])
    self.assertEquals((1425340800000, 2.68), data[1])
    self.assertEquals((1426291200000, 3.55), data[2])
    self.assertEquals((1426896000000, 3.21), data[3])
    self.assertEquals((1427414400000, 3.02), data[4])

  def test_winrate(self):
    """Extract daily winrate"""
    winrate_trend = self.trend.get('winrate')
    data = winrate_trend.data_day
    self.assertEquals(5, len(data))
    self.assertEquals((1425254400000, 0.5), data[0])
    self.assertEquals((1425340800000, 0.0), data[1])
    self.assertEquals((1426291200000, 1.0), data[2])
    self.assertEquals((1426896000000, 0.0), data[3])
    self.assertEquals((1427414400000, 0.0), data[4])

  def test_winrate_comulative(self):
    """Extract day comulative winrate"""
    winrate_trend = self.trend.get('winrate')
    data = winrate_trend.data_day_comulative
    self.assertEquals(5, len(data))
    self.assertEquals((1425254400000, 0.5), data[0])
    self.assertEquals((1425340800000, 0.25), data[1])
    self.assertEquals((1426291200000, 0.63), data[2])
    self.assertEquals((1426896000000, 0.56), data[3])
    self.assertEquals((1427414400000, 0.5), data[4])


if __name__ == "__main__":
  unittest.main()

