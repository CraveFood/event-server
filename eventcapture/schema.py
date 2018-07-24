EVENT = {
    'event': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
    },
    'user_id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'business_id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
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
}
