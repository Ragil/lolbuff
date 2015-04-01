import os

raw_match_history = None

with open(os.path.join(os.path.dirname(__file__), "match_history.json"), "r") as f:
  raw_match_history = f.read()

