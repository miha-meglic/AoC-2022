import aocd
from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def calc_points(opponent: Move, move: Move) -> int:
    if opponent == Move.ROCK and move == Move.PAPER or opponent == Move.PAPER and move == Move.SCISSORS or opponent == Move.SCISSORS and move == Move.ROCK:
        return 6 + move.value
    elif opponent == move:
        return 3 + move.value
    else:
        return move.value


move_map = {
    'A': Move.ROCK,
    'B': Move.PAPER,
    'C': Move.SCISSORS,
    'X': Move.ROCK,
    'Y': Move.PAPER,
    'Z': Move.SCISSORS,
}

data = aocd.get_data(day=2, year=2022)
score = 0

for move in data.splitlines():
    opp, sug = move.split(' ')
    opp = move_map[opp]
    sug = move_map[sug]

    score += calc_points(opp, sug)

print(f'Score: {score}')
# aocd.submit(score, part='a', day=2, year=2022)
