from datetime import datetime


def coerce_to_now(timestamp=None):
    if not timestamp or timestamp == 'empty':
        return datetime.utcnow()
    return timestamp


EVENT = {
    'event': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'user_id': {
        'type': 'integer',
    },
    'business_id': {
        'type': 'integer',
    },
    'session_id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'device_id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'segmentation': {
        'type': 'dict',
    },
    'timestamp': {
        'type': 'datetime',
        'default': 'empty',
        'coerce': coerce_to_now,
    },

}
