import webapp2
import json

class BaseRequestHandler(webapp2.RequestHandler):
  """Providing common helpers and decorators for request handlers"""

  def __init__(self):
    """Initialize handler"""
    self._regions = ['BR', 'EUNE', 'EUW', 'KR', 'LAN',
        'LAS', 'NA', 'OCE', 'RU', 'TR']

  def has_valid_region(self):
    """Return True if the request has a valid region parameter. False otherwise."""
    if self.request.get('region') not in self._regions:
      self.base_request(error_msg)
      return False

    return True

  def ensure_param(self, func):
    """Decorator to verify that a given parameter is set

    param_name -- str : the name of the parameter
    error_msg -- str : the error message to use as response
    """
    def check(param_name, error_msg=None):
      if not error_msg:
        error_msg = 'Invalid parameter "%s"' % param_name

      value = self.request.get(param_name)
      if not value or (isinstance(value, str) and not value.strip()):
        self.bad_request(error_msg)
        return

      # all good, proceed to func
      func()

    return check

  def bad_request(self, error_msg):
    """Respond with http 400 bad request"""
    self.respond_as_json({
      'error_msg' : error_msg
    }, 400)


  def respond_as_json(self, data, status):
    """Write a json response back to the client"""
    self.response.status = status
    self.response.write(json.dumps(data, default = lambda o: o.__dict__))
    self.response.headers['Content-Type'] = 'text/json;charset=utf-8'
