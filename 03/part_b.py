import aocd

data = aocd.get_data(day=3, year=2022)


def get_priority(item: str) -> int:
    if ord(match) < ord('a'):
        return ord(match) - ord('A') + 1 + 26
    else:
        return ord(match) - ord('a') + 1


priority_sum = 0

data = data.splitlines()
data = zip(data[0::3], data[1::3], data[2::3])

for bp in data:
    match = (set(bp[0]) & set(bp[1]) & set(bp[2])).pop()
    priority_sum += get_priority(match)

print(f'Sum of group priorities: {priority_sum}')
# aocd.submit(priority_sum, part='b', day=3, year=2022)
