import props
import logging

from google.appengine.api import users
from base_request_handler import BaseRequestHandler

class Handler(BaseRequestHandler):
  """Handler to update admin config"""

  def get(self, *args, **kwargs):
    """Initilize config if it doesn't already exist, otherwise update it"""
    user = users.get_current_user()

    if not args[0]:
      logging.error("%s tried to create global config without api_key" %
          user.email())
      return

    if not self.config:
      logging.warning("%s created new global config with api_key %s" %
          (user.email(), args[0]))
      props.init_config(args[0])

    else:
      logging.warning("%s tried to create global config but already exist" %
          user.email())

