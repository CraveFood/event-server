import os

from eve.auth import BasicAuth


USERNAME = os.getenv('EVENT_CAPTURE_USERNAME', 'admin')
PASSWORD = os.getenv('EVENT_CAPTURE_PASSWORD', 'secret')


class Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == USERNAME and password == PASSWORD
