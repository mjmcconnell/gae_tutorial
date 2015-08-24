# local imports
from webapp2 import Route


ROUTES = [
    Route('/', 'app.handlers.templates.LandingPage', name="landing_page"),
    Route('/page_two', 'app.handlers.templates.PageTwo', name="page_two"),
]
