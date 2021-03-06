from datetime import datetime


def coerce_to_now(timestamp=None):
    if not timestamp or timestamp == "empty":
        return datetime.utcnow()
    return timestamp


EVENT = {
    "name": {"type": "string", "minlength": 1, "maxlength": 100, "required": True},
    "segmentation": {"type": "dict", "required": True},
    "user_id": {"type": "integer"},
    "business_id": {"type": "integer"},
    "session_id": {"type": "string", "nullable": True, "empty": True},
    "device_id": {"type": "string", "nullable": True, "empty": True},
    "whitelabel": {"type": "string", "nullable": True, "empty": True},
    "timestamp": {"type": "datetime", "default": "empty", "coerce": coerce_to_now},
}
