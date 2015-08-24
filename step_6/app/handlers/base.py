"""Template handlers, for injecting python into html templates.
"""

# stdlib imports
from datetime import date

# third party imports
import jinja2
import webapp2

# local imports
from app import config
from app.models.messages import Message


class TemplateHandler(webapp2.RequestHandler):

    template = None

    def _get_jinja_template(self, template_file):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(config.TEMPLATE_DIR),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
        ).get_template(template_file)

    def get(self):
        """Default functionality for the get method
        """
        self.render(self.template)

    def render(self, template_file):
        """Handles setting the template values and rendering of the template.
        """
        # Grab template
        template = self._get_jinja_template(template_file)
        # Sent jinja variables
        template_values = {
            'date': date.today(),
            'get_data': self.request.GET,
            'post_data': self.request.POST,
            'messages': Message.query().fetch(),
        }
        # Write reponse to the browser
        self.response.write(template.render(template_values))
