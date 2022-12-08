import numpy as np
import aocd


def calculateScenicScore(trees: list[list[str]], x: int, y: int) -> int:
    height = trees[y][x]
    score = 1

    tr = 0
    for nx in range(x + 1, len(trees[y])):
        tr += 1
        if trees[y][nx] >= height:
            break
    score *= tr if tr != 0 else 1

    tr = 0
    for nx in range(x - 1, -1, -1):
        tr += 1
        if trees[y][nx] >= height:
            break
    score *= tr if tr != 0 else 1

    tr = 0
    for ny in range(y + 1, len(trees)):
        tr += 1
        if trees[ny][x] >= height:
            break
    score *= tr if tr != 0 else 1

    tr = 0
    for ny in range(y - 1, -1, -1):
        tr += 1
        if trees[ny][x] >= height:
            break
    score *= tr if tr != 0 else 1

    return score


data = aocd.get_data(day=8, year=2022).splitlines()
scores = np.zeros((len(data), len(data[0])))

for x in range(len(data[0])):
    for y in range(len(data)):
        scores[y][x] = calculateScenicScore(data, x, y)

unique = np.unique(scores)
maxScore = int(max(unique))

print(f'Max scenic score: {maxScore}')
# aocd.submit(maxScore, part='b', day=8, year=2022)
