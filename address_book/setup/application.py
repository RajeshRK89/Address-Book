import os.path
import json
from django.conf import settings


class Application(object):
    """
    Base application class.

    This is subclassed by each app to provide a customisable container for an
    app's views and permissions.
    """

    app_name = None
    name = None

    app_path = None

    include_url = True

    hidable_feature_name = None
    permissions_map = {}

    default_permissions = None

    def get_urls(self):
        """
        Return the url patterns for this app.
        """
        return []
