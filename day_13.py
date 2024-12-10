"""Day 13: Knights of the Dinner Table"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict
import itertools


def main():
    """Solve day 13 puzzles."""
    with open("data/day_13.txt", encoding="ascii") as input_file:
        puzzle_input = [line.rstrip() for line in input_file.readlines()]

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    attendees = parse(puzzle_input)
    happiness = max(
        compute_happiness(arrangement, attendees)
        for arrangement in itertools.permutations(attendees.keys())
    )

    return happiness


def star_2(puzzle_input):
    """Solve second puzzle."""
    attendees = parse(puzzle_input)
    attendees["myself"] = {}

    for attendee, preferences in attendees.items():
        attendees["myself"][attendee] = 0
        preferences["myself"] = 0

    happiness = max(
        compute_happiness(arrangement, attendees)
        for arrangement in itertools.permutations(attendees.keys())
    )

    return happiness


def compute_happiness(arrangement, attendees):
    """Compute the total happiness of a given arrangement."""
    happiness = sum(
        attendees[attendee][arrangement[(i - 1) % len(arrangement)]]
        + attendees[attendee][arrangement[(i + 1) % len(arrangement)]]
        for i, attendee in enumerate(arrangement)
    )

    return happiness


def parse(puzzle_input):
    """Parse puzzle input."""
    attendees = defaultdict(dict)

    for line in puzzle_input:
        words = line.rstrip(".").split()
        happiness = int(words[3]) if words[2] == "gain" else -int(words[3])
        attendees[words[0]][words[-1]] = happiness

    return dict(attendees)


if __name__ == "__main__":
    main()
