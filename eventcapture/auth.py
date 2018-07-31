import os

from eve.auth import BasicAuth
from eventcapture.settings import USERNAME, PASSWORD


class Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == USERNAME and password == PASSWORD
