from test_framework import generic_test
import collections


def examine_buildings_with_sunset(sequence):
    BuildingsWithHeight = collections.namedtuple(
        'BuildingsWithHeight', ('id', 'height'))

    buildings = []

    for building_id, height in enumerate(sequence):
        while buildings and buildings[-1].height <= height:
            buildings.pop()

        buildings.append(BuildingsWithHeight(building_id, height))

    return [b.id for b in reversed(buildings)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
