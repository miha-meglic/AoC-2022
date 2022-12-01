from functools import reduce

max = [0, 0, 0]

with open('elves_in.txt') as f:
    sum = 0
    for line in f:
        if len(line) <= 1:
            if sum > min(max):
                max[max.index(min(max))] = sum

            sum = 0
            continue

        sum += int(line[:-1])

if sum > min(max):
    max[max.index(min(max))] = sum

total = reduce(lambda a, b: a + b, max)
print(total)
