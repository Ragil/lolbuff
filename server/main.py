import webapp2

from api.app.trends_api_handler import Handler as TrendAPIHandler

api = webapp2.WSGIApplication([
  ('/api/trends', TrendAPIHandler),
], debug=True)
