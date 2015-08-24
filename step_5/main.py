"""Template handlers, for injecting python into html templates.
"""

# stdlib imports
import os
from datetime import date

# third party imports
import jinja2
import webapp2
from google.appengine.ext import ndb


# Set up the jinja configuration
JINJA_ENVIRONMENT = jinja2.Environment(
    # Tell jinja where to look for the template files
    loader=jinja2.FileSystemLoader(
        os.path.join(
            # This simply returns the current location of the main.py file
            # in your local file system.
            # For example on my machine it would return:
            #       /users/mark/python_projects/gae_tutorial/step_3/
            os.path.dirname(__file__),
            # templates folder
            'templates'
        )
    )
)


class Message(ndb.Model):
    """Datastore table, to store a visitors message
    """

    content = ndb.TextProperty()


class LandingPage(webapp2.RequestHandler):
    """Handles requests for the landing page
    """

    def get(self):
        # Define the variables we want to be available in the template
        template_values = {
            'date': date.today(),
            'get_data': self.request.GET,
            'post_data': self.request.POST,
            'messages': Message.query().fetch(),
        }

        # Grab the contents of the template
        template = JINJA_ENVIRONMENT.get_template('index.html')

        # Write out the html from the template with the variables populated
        self.response.write(template.render(template_values))

    def post(self):
        """Passes the request data to the render method
        """
        # Get the massage content from the post data
        content = self.request.POST.get('content')
        # Store the message content in the datastore for persistent storage
        Message(content=content).put()
        # Use the get method to render the landing page template as normal
        self.get()


class PageTwo(webapp2.RequestHandler):
    """Handles requests for the landing page
    """

    def get(self):
        # Grab the contents of the template
        template = JINJA_ENVIRONMENT.get_template('page_two.html')

        # Write out the html from the template with the variables populated
        self.response.write(template.render())


# Assign routes to the python classes above
app = webapp2.WSGIApplication(
    [
        ('/', LandingPage),
        ('/page_two', PageTwo),
    ]
)
