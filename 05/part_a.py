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

    for _ in range(int(count)):
        crate = cols[int(fr) - 1].pop()
        cols[int(to) - 1].append(crate)

tos = ''
for stack in cols:
    tos += stack[-1]

print(f'Top of stacks: {tos}')
# aocd.submit(tos, part='a', day=5, year=2022)
