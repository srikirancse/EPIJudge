import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people):
    age_count = collections.Counter([p.age for p in people])
    age_to_offset, offset = {}, 0

    for age, count in age_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:
        form_age = next(iter(age_to_offset))
        from_idx = age_to_offset[form_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[to_age]

        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]

        age_count[to_age] -= 1

        if age_count[to_age]:
            age_to_offset[to_age] += 1
        else:
            del age_to_offset[to_age]



print(group_by_age(list(
        map(lambda x: Person(x[0], x[1]),
            [
                [13, "Oliver"], [4, "Quincy"], [10, "Bob"], [27, "Quincy"], [11, "Sam"], [13, "Frank"],
                [4, "Mary"], [13, "Thomas"]
            ]))))


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
