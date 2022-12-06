import aocd


def areAllUnique(word: str) -> bool:
    for (i, char1) in enumerate(word):
        for char2 in word[i+1:]:
            if char1 == char2:
                return False
    return True


data = aocd.get_data(day=6, year=2022)

count = 4
buff = data[:4]

for c in data[4:]:
    if areAllUnique(buff):
        break

    buff = buff[1:]
    buff += c
    count += 1

print(f'Character count: {count}')
# aocd.submit(count, part='a', day=6, year=2022)
