import os

class LocalConfig():
  """Holds local application config"""

  def __init__(self):
    """Default configuration"""

    if "lol_api_key" not in os.environ:
      raise ValueError('Missing environment variable "lol_api_key"')
    self.lol_api_key = os.environ["lol_api_key" ]


config = LocalConfig()
