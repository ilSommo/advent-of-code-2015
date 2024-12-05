"""Day 7: Some Assembly Required"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"


def main():
    """Solve day 7 puzzles."""
    with open("data/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.readlines()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle"""
    wires = {}
    puzzle = puzzle_input.copy()

    while puzzle:
        line = puzzle.pop(0)
        input_wires, output = line.rstrip().split(" -> ")
        result = compute_instruction(wires, input_wires)

        if result is not None:
            wires[output] = result

        else:
            puzzle.append(line)

    return wires["a"]


def star_2(puzzle_input):
    """Solve second puzzle."""
    wires = {"b": star_1(puzzle_input)}
    puzzle = puzzle_input.copy()

    while puzzle:
        line = puzzle.pop(0)
        input_wires, output = line.rstrip().split(" -> ")

        if output != "b":
            result = compute_instruction(wires, input_wires)

            if result is not None:
                wires[output] = result

            else:
                puzzle.append(line)

    return wires["a"]


def compute_instruction(wires, input_wires):
    """Compute result of an instruction."""
    instruction = input_wires.split()

    try:
        match len(instruction):
            case 1:
                return (
                    int(instruction[0])
                    if instruction[0].isnumeric()
                    else wires[instruction[0]]
                )

            case 2:
                return ~wires[instruction[1]]

            case 3:
                operand_0 = (
                    int(instruction[0])
                    if instruction[0].isnumeric()
                    else wires[instruction[0]]
                )
                operand_1 = (
                    int(instruction[2])
                    if instruction[2].isnumeric()
                    else wires[instruction[2]]
                )

                return compute_ternary_instruction(
                    instruction[1], operand_0, operand_1
                )

    except KeyError:
        return None


def compute_ternary_instruction(operator, operand_0, operand_1):
    """Compute result of a ternary instruction."""
    match operator:
        case "AND":
            return operand_0 & operand_1

        case "OR":
            return operand_0 | operand_1

        case "LSHIFT":
            return operand_0 << operand_1

        case "RSHIFT":
            return operand_0 >> operand_1


if __name__ == "__main__":
    main()
