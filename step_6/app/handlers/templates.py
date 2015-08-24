"""Template handlers, for injecting python into html templates.
"""
# local imports
from app.models.messages import Message
from app.handlers.base import TemplateHandler


class LandingPage(TemplateHandler):
    """Handles requests for the landing page
    """
    template = 'index.html'

    def post(self):
        """Passes the request data to the render method
        """
        # Get the massage content from the post data
        content = self.request.POST.get('content')
        # Store the message content in the datastore for persistent storage
        Message(content=content).put()

        self.get()


class PageTwo(TemplateHandler):
    """Handles requests for page two
    """

    template = 'page_two.html'
