"""Day 22: Wizard Simulator 20XX"""

__author__ = "Martino M. L. Pulici <martinomarelakota@yahoo.it>"
__date__ = "2024"
__license__ = "MIT"

from collections import deque
from dataclasses import dataclass, field
import copy

COSTS = (53, 73, 113, 173, 229)


@dataclass
class Status:
    """Status of the spells."""

    shield: int = 0
    poison: int = 0
    recharge: int = 0


@dataclass
class State:
    """State of the game."""

    boss_points: int
    boss_damage: int
    player_points: int
    mana: int
    spent: int = 0
    status: Status = field(default_factory=Status)
    player_turn: bool = True


def main():
    """Solve day 22 puzzles."""
    with open("data/day_22.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzles."""
    boss = load_boss(puzzle_input)
    player = [50, 500]

    games = deque([State(boss[0], boss[1], player[0], player[1])])
    min_mana = float("inf")

    while games:
        game = games.popleft()

        if game.player_points <= 0 or game.spent >= min_mana:
            continue

        if game.boss_points <= 0:
            min_mana = game.spent
            continue

        games.extend(play_turn(game))

    return min_mana


def star_2(puzzle_input):
    """Solve second puzzle."""
    boss = load_boss(puzzle_input)
    player = [50, 500]

    games = deque([State(boss[0], boss[1], player[0], player[1])])
    min_mana = float("inf")

    while games:
        game = games.popleft()

        if game.player_points <= 0 or game.spent >= min_mana:
            continue

        if game.boss_points <= 0:
            min_mana = game.spent
            continue

        games.extend(play_turn(game, True))

    return min_mana


def play_turn(state, hard=False):
    """Play game turn."""
    if hard and state.player_turn:
        state.player_points -= 1

    if state.status.poison:
        state.boss_points -= 3
        state.status.poison -= 1

    if state.boss_points <= 0 or state.player_points <= 0:
        return [state]

    armor = 0

    if state.status.shield:
        armor = 7
        state.status.shield -= 1

    if state.status.recharge:
        state.mana += 101
        state.status.recharge -= 1

    states = []

    if state.player_turn:
        state.player_turn = False

        for i, cost in enumerate(COSTS):
            if cost > state.mana:
                continue

            new_state = copy.deepcopy(state)

            match i:
                case 0:
                    new_state.boss_points -= 4

                case 1:
                    new_state.boss_points -= 2
                    new_state.player_points += 2

                case 2:
                    if state.status.shield:
                        continue

                    new_state.status.shield = 6

                case 3:
                    if state.status.poison:
                        continue

                    new_state.status.poison = 6

                case 4:
                    if state.status.recharge:
                        continue

                    new_state.status.recharge = 5

            new_state.mana -= cost
            new_state.spent += cost
            states.append(new_state)

    else:
        state.player_turn = True
        state.player_points -= max(1, state.boss_damage - armor)
        states = [state]

    return states


def load_boss(puzzle_input):
    """Load boss stats from input."""
    points = int(puzzle_input[0].split()[-1])
    damage = int(puzzle_input[1].split()[-1])

    return points, damage


if __name__ == "__main__":
    main()
