import aocd

data = aocd.get_data(day=1, year=2022)

max = 0
sum = 0

for line in data.splitlines():
    if len(line) == 0:
        if sum > max:
            max = sum

        sum = 0
        continue

    sum += int(line)

if sum > max:
    max = sum

print(f'Max calories: {max}')
# aocd.submit(max, part='a', day=1, year=2022)
