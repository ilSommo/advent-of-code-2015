"""Day 12: Corporate Policy"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools
import json


def main():
    """Solve day 12 puzzles."""
    with open("data/day_12.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    data = flatten(json.loads(puzzle_input))

    return sum(elem if isinstance(elem, int) else 0 for elem in data)


def star_2(puzzle_input):
    """Solve second puzzle."""
    data = flatten_red(json.loads(puzzle_input))

    return sum(elem if isinstance(elem, int) else 0 for elem in data)


def flatten(data):
    """Recursively flatten json data."""
    if isinstance(data, dict):
        return list(itertools.chain(data.keys(), flatten(list(data.values()))))

    if isinstance(data, list):
        return list(
            itertools.chain.from_iterable([flatten(elem) for elem in data])
        )

    return [data]


def flatten_red(data):
    """Recursively flatten json data."""
    if isinstance(data, dict):
        if "red" in data.keys() or "red" in data.values():
            return []

        return list(
            itertools.chain(data.keys(), flatten_red(list(data.values())))
        )

    if isinstance(data, list):
        return list(
            itertools.chain.from_iterable([flatten_red(elem) for elem in data])
        )

    return [data]


if __name__ == "__main__":
    main()
