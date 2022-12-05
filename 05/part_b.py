import aocd

data = aocd.get_data(day=5, year=2022).splitlines()

numOfCols = (len(data[0]) + 1) // 4
cols = list()

for _ in range(numOfCols):
    cols.append(list())

i = 0
while len(data[i+1]) != 0:
    for j, crate in enumerate(data[i][1::4]):
        if (crate != ' '):
            cols[j].insert(0, crate)
    i += 1

for move in data[i+2:]:
    _, count, _, fr, _, to = move.split(' ')

    count, fr, to = int(count), int(fr), int(to)

    crates = cols[fr - 1][-count:]
    cols[fr - 1] = cols[fr - 1][:-count]
    cols[to - 1] += crates

tos = ''
for stack in cols:
    tos += stack[-1]

print(f'Top of stacks: {tos}')
# aocd.submit(tos, part='b', day=5, year=2022)
