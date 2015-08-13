"""Template handlers, for injecting python into html templates.
"""
from google.appengine.api import users

# local imports
from app.models.users import User
from app.handlers.base import TemplateHandler


class LandingPage(TemplateHandler):
    """Handles requests for the landing page
    """
    template = 'index.html'

    def post(self):
        """Passes the request data to the render method
        """
        user = users.get_current_user()
        msg = self.request.POST.get('msg')
        db_record = User.query(User.email == user.email()).get()
        if db_record is None:
            db_record = User(email=user.email).put().get()

        db_record.msg = msg
        db_record.put()

        self.get()


class PageTwo(TemplateHandler):
    """Handles requests for page two
    """

    template = 'page_two.html'
