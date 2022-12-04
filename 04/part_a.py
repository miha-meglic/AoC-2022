import aocd


def isRangeEnveloped(range1: str, range2: str) -> bool:
    sr1 = range1.split('-')
    sr2 = range2.split('-')

    if int(sr1[0]) <= int(sr2[0]) and int(sr1[1]) >= int(sr2[1]):
        return True

    if int(sr2[0]) <= int(sr1[0]) and int(sr2[1]) >= int(sr1[1]):
        return True

    return False


data = aocd.get_data(day=4, year=2022)

enveloping_pairs = 0

for line in data.splitlines():
    line = line.split(',')
    r1 = line[0]
    r2 = line[1]

    if (isRangeEnveloped(r1, r2)):
        enveloping_pairs += 1

print(f'Enveloping pairs: {enveloping_pairs}')
# aocd.submit(enveloping_pairs, part='a', day=4, year=2022)
