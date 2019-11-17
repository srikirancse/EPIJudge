import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A):
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))
    endpoints = [p for a in A for p in (
        Endpoint(a.start, True), Endpoint(a.finish, False))]
    endpoints.sort(key=lambda x: (x.time, not x.is_start))

    simultaneous_events, max_events = 0, 0

    for e in endpoints:
        if e.is_start:
            simultaneous_events += 1
            max_events = max(max_events, simultaneous_events)

        else:
            simultaneous_events -= 1

    return max_events



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
