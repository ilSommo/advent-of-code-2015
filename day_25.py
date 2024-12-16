"""Day 25: Let It Snow"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 25 puzzles."""
    with open("data/day_25.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    r, c = load_coordinates(puzzle_input)

    index = int((c**2 + 2 * c * r - c + r**2 - 3 * r + 2) / 2)
    value = 20151125

    for _ in range(index - 1):
        value = value * 252533 % 33554393

    return value


def load_coordinates(puzzle_input):
    """Load coordinates from puzzle input."""
    row = int(puzzle_input.split()[-3][:-1])
    column = int(puzzle_input.split()[-1][:-1])

    return row, column


if __name__ == "__main__":
    main()
