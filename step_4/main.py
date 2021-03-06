"""Template handlers, for injecting python into html templates.
"""

# stdlib imports
import os
from datetime import date

# third party imports
import jinja2
import webapp2


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


class LandingPage(webapp2.RequestHandler):
    """Handles requests for the landing page
    """

    def get(self):
        # Define the variables we want to be available in the template
        template_values = {
            'date': date.today(),
            'get_data': self.request.GET,
            'post_data': self.request.POST,
        }

        # Grab the contents of the template
        template = JINJA_ENVIRONMENT.get_template('index.html')

        # Write out the html from the template with the variables populated
        self.response.write(template.render(template_values))

    def post(self):
        """Lets the get method handle everything
        """
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
