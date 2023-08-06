import time
from contextlib import contextmanager

measurements = []
measure_enabled = False


def enable_measure(s: bool):
    global measure_enabled
    measure_enabled = s


@contextmanager
def measure(name):
    global measure_enabled
    if measure_enabled:
        start_time = time.time()
        yield
        end_time = time.time()
        elapsed_time = end_time - start_time
        measurements.append((name, elapsed_time))
    else:
        yield


def measure_decorator(func):
    def wrapper(*args, **kwargs):
        with measure(func.__name__):
            return func(*args, **kwargs)

    return wrapper


def flush():
    for m in measurements:
        print(m[0], m[1])
