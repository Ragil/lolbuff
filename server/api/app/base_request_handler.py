import webapp2
import json
import logging
import props

class BaseRequestHandler(webapp2.RequestHandler):
  """Providing common helpers and decorators for request handlers"""

  def __init__(self, request, response):
    """Initialize handler"""
    self.config = props.get_config()
    self.initialize(request, response)
    self._regions = ['br', 'eune', 'euw', 'kr', 'lan',
        'las', 'na', 'oce', 'ru', 'tr']

  def has_valid_region(self):
    """Return True if the request has a valid region parameter. False otherwise."""
    if self.request.get('region') not in self._regions:
      self.bad_request('Invalid region "%s". Valid regions %s' %
          (self.request.get('region'), self._regions))
      return False

    return True

  @staticmethod
  def ensure_param(param_name, error_msg=None):
    """Decorator to verify that a given parameter is set

    param_name -- str : the name of the parameter
    error_msg -- str : the error message to use as response
    """
    if not error_msg:
      error_msg = 'Missing parameter "%s"' % param_name

    def decorator(func):
      def check(self, *args, **kwargs):

        value = self.request.get(param_name)
        if not value or (isinstance(value, str) and not value.strip()):
          self.bad_request(error_msg)
          return

        # all good, proceed to func
        func(self, args, kwargs)

      return check
    return decorator

  def bad_request(self, error_msg):
    """Respond with http 400 bad request"""
    self.respond_as_json({
      'error_msg' : error_msg
    }, 400)


  def respond_as_json(self, data, status):
    """Write a json response back to the client"""
    self.response.status = status
    self.response.write(json.dumps(data))
    self.response.headers['Content-Type'] = 'text/json;charset=utf-8'
