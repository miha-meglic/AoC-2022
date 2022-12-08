from node import File, Dir
import aocd

data = aocd.get_data(day=7, year=2022)[2:]

root = Dir('/', None)
current = root

for command in data.split('\n$ '):
    lines = command.splitlines()
    cmd = lines[0]

    if cmd.split(' ')[0] == 'cd':
        path = cmd.split(' ')[1]
        if path == '/':
            current = root
        elif path == '..':
            current = current.getParent()
            if current == None:
                current = root
        else:
            current = current.getDir(path)
            if current == None:
                raise Exception(f'Unknown location: `{path}`')
    elif cmd == 'ls':
        for line in lines[1:]:
            line = line.split(' ')
            if line[0] == 'dir':
                current.addDir(line[1])
            else:
                current.addFile(line[1], int(line[0]))
    else:
        print(f'Unknown command: `{cmd}`')

freeSpace = 70000000 - root.getSize()
requiredSpace = 30000000

spaceToFree = requiredSpace - freeSpace

dirs = root.getSmallestDirsBiggerThan(spaceToFree)
minSize = 70000000

for dir in dirs:
    s = dir.getSize()
    if s < minSize:
        minSize = s

print(f'Size of dir to delete: {minSize} (required {spaceToFree})')
# aocd.submit(minSize, part='b', day=7, year=2022)
