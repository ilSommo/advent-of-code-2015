"""Day 18: Like a GIF For Your Yard"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

import itertools


def main():
    """Solve day 18 puzzles."""
    with open("data/day_18.txt", encoding="ascii") as input_file:
        puzzle_input = [line.rstrip() for line in input_file.readlines()]

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    n_rows = len(puzzle_input)
    n_cols = len(puzzle_input[0])
    lights = load_map(puzzle_input)

    for _ in range(100):
        lights = compute_step(lights, (n_rows, n_cols))

    n_lights = len(lights)

    return n_lights


def star_2(puzzle_input):
    """Solve second puzzle."""
    n_rows = len(puzzle_input)
    n_cols = len(puzzle_input[0])
    always_on = {
        0 + 0j,
        0 + (n_cols - 1) * 1j,
        (n_rows - 1) + 0j,
        (n_rows - 1) + (n_cols - 1) * 1j,
    }
    lights = load_map(puzzle_input) | always_on

    for _ in range(100):
        lights = compute_step(lights, (n_rows, n_cols)) | always_on

    n_lights = len(lights)

    return n_lights


def compute_step(lights, dims):
    """Compute step result."""
    new_lights = set()

    for i, j in itertools.product(range(dims[0]), range(dims[1])):
        light = i + j * 1j in lights
        neighbors = sum(
            neighbor in lights for neighbor in get_neighbors(i + j * 1j)
        )

        if light and not 2 <= neighbors < 4:
            light = False

        elif not light and neighbors == 3:
            light = True

        if light:
            new_lights.add(i + j * 1j)

    return new_lights


def get_neighbors(light):
    """Get all neighbors of a light."""
    neighbors = {
        light + (i + j * 1j)
        for i, j in itertools.product(range(-1, 2), repeat=2)
    } - {light}

    return neighbors


def load_map(puzzle_input):
    """Load map from puzzle_input."""
    lights = {
        i + j * 1j
        for i, line in enumerate(puzzle_input)
        for j, elem in enumerate(line)
        if elem == "#"
    }

    return lights


if __name__ == "__main__":
    main()
