import logging
from functools import wraps

def log_call(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        logging.getLogger(function.__module__).info("Calling %s",function.__name__)
        return function(*args,**kwargs)
    return wrapper
