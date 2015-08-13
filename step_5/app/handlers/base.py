"""Template handlers, for injecting python into html templates.
"""
# third party imports
import jinja2
import webapp2
from google.appengine.api import users

# local imports
from app import config
from app.models.users import User


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

        template = self._get_jinja_template(template_file)

        template_values = {
            'login_url': users.create_login_url('/'),
            'logout_url': users.create_logout_url,
            'user': users.get_current_user(),
            'users': User.query().fetch()
        }

        self.response.write(template.render(template_values))
