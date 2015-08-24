"""Base datastore models and queries
"""
# third-party imports
from google.appengine.ext import ndb


class Message(ndb.Model):
    """Datastore table, to store a visitors message
    """

    content = ndb.TextProperty()
