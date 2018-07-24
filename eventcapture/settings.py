import os

from eventcapture.schema import EVENT

MONGO_HOST = os.getenv('EVENT_CAPTURE_MONGO_URI', 'mongo')

MONGO_DBNAME = 'event'

RESOURCE_METHODS = ['POST']

event = {
    'schema': EVENT,
}

DOMAIN = {'event': event}