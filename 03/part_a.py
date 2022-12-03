import aocd

data = aocd.get_data(day=3, year=2022)

priority_sum = 0

for bp in data.splitlines():
    c1 = bp[:len(bp)//2]
    c2 = bp[len(bp)//2:]

    match = (set(c1) & set(c2)).pop()

    if ord(match) < ord('a'):
        priority_sum += ord(match) - ord('A') + 1 + 26
    else:
        priority_sum += ord(match) - ord('a') + 1

print(f'Sum of priorities: {priority_sum}')
# aocd.submit(priority_sum, part='a', day=3, year=2022)
