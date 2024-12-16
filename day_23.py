"""Day 23: Opening the Turing Lock"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 23 puzzles."""
    with open("data/day_23.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    registers = {"a": 0, "b": 0}
    instructions = load_instructions(puzzle_input)
    i = 0

    while i < len(instructions):
        registers, i = perform_instruction(instructions, i, registers)

    return registers["b"]


def star_2(puzzle_input):
    """Solve second puzzle."""
    registers = {"a": 1, "b": 0}
    instructions = load_instructions(puzzle_input)
    i = 0

    while i < len(instructions):
        registers, i = perform_instruction(instructions, i, registers)

    return registers["b"]


def load_instructions(puzzle_input):
    """Load instructions from input."""
    instructions = tuple(line.split() for line in puzzle_input)

    return instructions


def perform_instruction(instructions, i, registers):
    """Perform instruction on registers."""
    instruction = instructions[i]
    i += 1

    match instruction[0]:
        case "hlf":
            registers[instruction[1][0]] //= 2

        case "tpl":
            registers[instruction[1][0]] *= 3

        case "inc":
            registers[instruction[1][0]] += 1

        case "jmp":
            i += int(instruction[1]) - 1

        case "jie":
            if registers[instruction[1][0]] % 2 == 0:
                i += int(instruction[2]) - 1

        case "jio":
            if registers[instruction[1][0]] == 1:
                i += int(instruction[2]) - 1

    return registers, i


if __name__ == "__main__":
    main()
