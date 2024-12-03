"""Day 6: Probably a Fire Hazard"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 6 puzzles."""
    with open("data/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle"""
    grid = [1000 * [-1] for _ in range(1000)]

    for line in puzzle_input:
        action, x_range, y_range = parse(line)

        match action:
            case "toggle":
                for i, j in itertools.product(x_range, y_range):
                    grid[i][j] *= -1

            case "on":
                for i, j in itertools.product(x_range, y_range):
                    grid[i][j] = 1

            case "off":
                for i, j in itertools.product(x_range, y_range):
                    grid[i][j] = -1

    total = sum(row.count(1) for row in grid)

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    grid = [1000 * [0] for _ in range(1000)]

    for line in puzzle_input:
        action, x_range, y_range = parse(line)

        match action:
            case "toggle":
                for i, j in itertools.product(x_range, y_range):
                    grid[i][j] += 2

            case "on":
                for i, j in itertools.product(x_range, y_range):
                    grid[i][j] += 1

            case "off":
                for i, j in itertools.product(x_range, y_range):
                    grid[i][j] = max(0, grid[i][j] - 1)

    total = sum(sum(row) for row in grid)

    return total


def parse(line):
    """Parse an instruction line"""
    split_line = line.split()
    action, start, end = (
        split_line[-4],
        split_line[-3].split(","),
        split_line[-1].split(","),
    )
    x_range = range(int(start[0]), int(end[0]) + 1)
    y_range = range(int(start[1]), int(end[1]) + 1)

    return action, x_range, y_range


if __name__ == "__main__":
    main()
