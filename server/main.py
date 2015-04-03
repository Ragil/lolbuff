import webapp2

from api.app.trends_api_handler import Handler as TrendAPIHandler
from api.app.admin_api_handler import Handler as AdminAPIHandler

api = webapp2.WSGIApplication([
  ('/api/trends', TrendAPIHandler),
  ('/api/admin/config/(.*)', AdminAPIHandler)
], debug=True)

