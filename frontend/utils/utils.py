from itertools import islice


def calculate_percentage(real_value, expected_value):
    return int((real_value / expected_value) * 100) if expected_value > 0 else 0

def chunks(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield [first] + list(islice(iterator, size - 1))
