"""Day 1: Not Quite Lisp"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 1 puzzles."""
    with open("data/day_1.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return puzzle_input.count("(") - puzzle_input.count(")")


def star_2(puzzle_input):
    """Solve second puzzle."""
    floor = 0

    for i, char in enumerate(puzzle_input):
        floor += (char == "(") - (char == ")")

        if floor < 0:
            return i + 1

    return 0


if __name__ == "__main__":
    main()
