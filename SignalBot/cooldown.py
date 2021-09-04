import time
from functools import wraps
from datetime import datetime, timedelta


def cooldown(*delta_args, **delta_kwargs):
    delta = timedelta(*delta_args, **delta_kwargs)
    def decorator(func):
        last_called = None
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = datetime.now()
            if last_called and (now - last_called < delta):
                return
            last_called = now
            return func(*args, **kwargs)
        return wrapper
    return decorator
