import numpy as np
import aocd

data = aocd.get_data(day=8, year=2022).splitlines()
visible = np.ndarray((len(data), len(data[0])), dtype=np.bool8)
visible.fill(True)
visible[1:-1, 1:-1] = False

# Top to bottom
heights = list(data[0])
for y in range(1, len(data) - 1):
    for x in range(len(data[0])):
        if data[y][x] > heights[x]:
            heights[x] = data[y][x]
            visible[y][x] = True

# Bottom to top
heights = list(data[-1])
for y in range(len(data) - 2, 0, -1):
    for x in range(len(data[0])):
        if data[y][x] > heights[x]:
            heights[x] = data[y][x]
            visible[y][x] = True

# Left to right
heights = [data[y][0] for y in range(len(data))]
for x in range(1, len(data[0]) - 1):
    for y in range(len(data)):
        if data[y][x] > heights[y]:
            heights[y] = data[y][x]
            visible[y][x] = True

# Right to left
heights = [data[y][len(data[0]) - 1] for y in range(len(data))]
for x in range(len(data[0]) - 2, 0, -1):
    for y in range(len(data)):
        if data[y][x] > heights[y]:
            heights[y] = data[y][x]
            visible[y][x] = True

# Count visible / not visible trees
uniq, cnt = np.unique(visible, return_counts=True)
unique = dict(zip(uniq, cnt))

print(f'Visible trees: {unique[True]}')
# aocd.submit(unique[True], part='a', day=8, year=2022)
