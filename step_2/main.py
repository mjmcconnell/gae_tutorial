"""Example of how we can use python to render html pages,
without the need for actual .html files.
"""

# stdlib imports
from datetime import date

# third party imports
import webapp2


class LandingPage(webapp2.RequestHandler):
    """Handles requests for the landing page
    """

    def get(self):
        self.response.write('<h1>Hello World</h1>')
        self.response.write('<p>I\'ve been called from the python handler at main.py</p>')

        self.response.write('<p>That means I can tell you todays date</p>')
        self.response.write('<p>%s</p>' % date.today())

        self.response.write('<a href="/page_two">click me</a> to go to page two')


class PageTwo(webapp2.RequestHandler):
    """Handles requests for page two.
    """

    def get(self):
        self.response.write('<h1>You found page two, whoop</h1>')
        self.response.write('<a href="/">click me</a> to go back to the landing page')

# Assign routes to the python classes above
app = webapp2.WSGIApplication(
    [
        ('/', LandingPage),
        ('/page_two', PageTwo),
    ]
)
