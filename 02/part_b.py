import aocd
from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def calc_points(opponent: Move, move: Move) -> int:
    if opponent == move:
        return 3 + move.value
    elif move == winning_move(opponent):
        return 6 + move.value
    else:
        return move.value


def winning_move(opponent: Move) -> Move:
    if opponent == Move.ROCK:
        return Move.PAPER
    elif opponent == Move.PAPER:
        return Move.SCISSORS
    else:
        return Move.ROCK


def loosing_move(opponent: Move) -> Move:
    if opponent == Move.ROCK:
        return Move.SCISSORS
    elif opponent == Move.PAPER:
        return Move.ROCK
    else:
        return Move.PAPER


move_map = {
    'A': Move.ROCK,
    'B': Move.PAPER,
    'C': Move.SCISSORS
}

data = aocd.get_data(day=2, year=2022)
score = 0

for move in data.splitlines():
    opp, sug = move.split(' ')
    opp = move_map[opp]

    if sug == 'X':
        sug = loosing_move(opp)
    elif sug == 'Z':
        sug = winning_move(opp)
    else:
        sug = opp

    score += calc_points(opp, sug)

print(f'Score: {score}')
# aocd.submit(score, part='b', day=2, year=2022)
