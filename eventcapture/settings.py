import os

from eventcapture.schema import EVENT

MONGO_HOST = os.getenv('EVENT_CAPTURE_MONGO_URI', 'mongo')
# MONGO_PORT = 27017
# MONGO_USERNAME = 'admin'
# MONGO_PASSWORD = 'admin'

MONGO_DBNAME = 'events'

RESOURCE_METHODS = ['POST']

events = {
    'schema': EVENT,
}

DOMAIN = {'events': events}
