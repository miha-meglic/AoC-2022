import aocd
from functools import reduce

data = aocd.get_data(day=1, year=2022)

max = [0, 0, 0]
sum = 0

for line in data.splitlines():
    if len(line) == 0:
        if sum > min(max):
            max[max.index(min(max))] = sum

        sum = 0
        continue

    sum += int(line)

if sum > min(max):
    max[max.index(min(max))] = sum

total = reduce(lambda a, b: a + b, max)

print(f'Top-3 calories sum: {total}')
# aocd.submit(max, part='b', day=1, year=2022)
