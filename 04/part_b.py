import aocd


def isRangeOverlapping(range1: str, range2: str) -> bool:
    sr1 = range1.split('-')
    sr2 = range2.split('-')

    if int(sr1[0]) <= int(sr2[0]) and int(sr1[1]) >= int(sr2[0]) or int(sr1[0]) <= int(sr2[1]) and int(sr1[1]) >= int(sr2[1]):
        return True

    if int(sr2[0]) <= int(sr1[0]) and int(sr2[1]) >= int(sr1[0]) or int(sr2[0]) <= int(sr1[1]) and int(sr2[1]) >= int(sr1[1]):
        return True

    return False


data = aocd.get_data(day=4, year=2022)

overlapping_pairs = 0

for line in data.splitlines():
    line = line.split(',')
    r1 = line[0]
    r2 = line[1]

    if (isRangeOverlapping(r1, r2)):
        overlapping_pairs += 1

print(f'Overlapping pairs: {overlapping_pairs}')
aocd.submit(overlapping_pairs, part='b', day=4, year=2022)
