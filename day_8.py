"""Day 8: Mastchsticks"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 8 puzzles."""
    with open("data/day_8.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    total = 0

    for line in puzzle_input:
        literal = line.rstrip()
        total += len(literal) - len(
            literal[1:-1].encode("ascii").decode("unicode_escape")
        )

    return total


def star_2(puzzle_input):
    """Solve second puzzle."""
    total = 0

    for line in puzzle_input:
        literal = line.rstrip()
        total += literal.count('"') + len(repr(literal)) - len(literal)

    return total


if __name__ == "__main__":
    main()
