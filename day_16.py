"""Day 16: Aunt Sue"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

COMPOUNDS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def main():
    """Solve day 16 puzzles."""
    with open("data/day_16.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    for line in puzzle_input:
        number, things = process_aunt(line)

        if check_things_1(things):
            return number

    return 0


def star_2(puzzle_input):
    """Solve second puzzle."""
    for line in puzzle_input:
        number, things = process_aunt(line)

        if check_things_2(things):
            return number

    return 0


def check_things_1(things):
    """Check if things are compatible."""
    for k, v in things.items():
        if COMPOUNDS[k] != v:
            return False

    return True


def check_things_2(things):
    """Check if things are compatible."""
    for k, v in things.items():
        if (
            k in ("cats", "trees")
            and COMPOUNDS[k] >= v
            or k in ("pomeranians", "goldfish")
            and COMPOUNDS[k] <= v
        ):
            return False

        if (
            k not in ("cats", "trees", "pomeranians", "goldfish")
            and COMPOUNDS[k] != v
        ):
            return False

    return True


def process_aunt(line):
    """Process input line."""
    name, string = line.split(": ", 1)
    number = int(name.split()[-1])

    things = {
        item.split(": ")[0]: int(item.split(": ")[1])
        for item in string.split(", ")
    }

    return number, things


if __name__ == "__main__":
    main()
