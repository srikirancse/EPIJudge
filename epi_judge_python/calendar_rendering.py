import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

    endpoints = [
        p for event in A for p in (Endpoint(event.start, True), Endpoint(event.finish, False))
    ]
    endpoints.sort(key=lambda endpoint: (endpoint.time, not endpoint.is_start))

    result = 0
    counter = 0

    for endpoint in endpoints:
        if endpoint.is_start:
            counter += 1
            result = max(result, counter)
        else:
            counter -= 1

    return result


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
