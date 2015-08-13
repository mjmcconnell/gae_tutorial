# third party imports
import webapp2

# local imports
from routes import ROUTES


# Assign routes to the python classes above
app = webapp2.WSGIApplication(
    ROUTES
)
