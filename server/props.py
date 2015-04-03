import os
from google.appengine.ext import ndb

class Config(ndb.Model):
  """Holds local application config"""
  lol_api_key = ndb.StringProperty()


def get_config():
  """Fetch configuration for the current request"""

  # testing env, get config from sys envs
  if os.environ["SERVER_NAME"] == "testbed.example.com":
    if 'lol_api_key' not in os.environ:
      raise ValueError('environment var "lol_api_key" is not defined')
    return Config(id="global", lol_api_key = os.environ['lol_api_key'])

  return ndb.Key(Config, "global").get()

def init_config(api_key):
  """Initialize first config entry for first application run"""
  config = Config(id="global", lol_api_key=api_key)
  config.put()

