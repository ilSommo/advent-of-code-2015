"""Day 14: Reindeer Olympics"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import defaultdict


def main():
    """Solve day 14 puzzles."""
    with open("data/day_14.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    reindeers = get_reindeers(puzzle_input)

    return max(compute_distance(reindeer, 2503) for reindeer in reindeers)


def star_2(puzzle_input):
    """Solve second puzzle."""
    reindeers = get_reindeers(puzzle_input)
    points = defaultdict(int)

    for i in range(1, 2504):
        distances = tuple(
            compute_distance(reindeer, i) for reindeer in reindeers
        )
        max_distance = max(distances)
        leaders = tuple(
            i
            for i, distance in enumerate(distances)
            if distance == max_distance
        )

        for leader in leaders:
            points[leader] += 1

    return max(points.values())


def compute_distance(reindeer, seconds):
    """Compute traveled distance."""
    speed, fly_time, rest_time = reindeer
    cycle_time = fly_time + rest_time

    return (
        seconds // cycle_time * speed * fly_time
        + min(seconds % cycle_time, fly_time) * speed
    )


def get_reindeers(puzzle_input):
    """Get reindeers from puzzle input."""
    return tuple(
        tuple(
            int(value)
            for value in (line.split()[3], line.split()[6], line.split()[13])
        )
        for line in puzzle_input
    )


if __name__ == "__main__":
    main()
