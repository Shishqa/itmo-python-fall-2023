import sys
import datetime
import functools
import logging

logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

log = logging.getLogger(__file__)
log.addHandler(stream_handler)


def timing(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log.info(f"running {func.__name__}")
        ts = datetime.datetime.now()
        res = func(*args, **kwargs)
        te = datetime.datetime.now()
        time_passed = (te - ts).total_seconds()
        log.info(f"done in {time_passed:2.4} seconds")
        return (time_passed, res)

    return wrapper
