max = 0

with open('elves_in.txt') as f:
    sum = 0
    for line in f:
        if len(line) <= 1:
            if sum > max:
                max = sum

            sum = 0
            continue

        sum += int(line[:-1])

if sum > max:
    max = sum

print(max)
