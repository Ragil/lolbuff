import os

raw_match_history = None
raw_summoner = None

with open(os.path.join(os.path.dirname(__file__), "match_history.json"), "r") as f:
  raw_match_history = f.read()

with open(os.path.join(os.path.dirname(__file__), "summoner.json"), "r") as f:
  raw_summoner = f.read()
