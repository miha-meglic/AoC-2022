class File:
    def __init__(self, name: str, size: int) -> None:
        self._name = name
        self._size = size

    def getName(self) -> str:
        return self._name

    def getSize(self) -> int:
        return self._size


class Dir:
    def __init__(self, name: str, parent: 'Dir') -> None:
        self._name = name
        self._parent = parent
        self._files = list()
        self._dirs = list()

    def getName(self) -> str:
        return self._name

    def getParent(self) -> 'Dir':
        return self._parent

    def getSize(self) -> int:
        size = 0

        for dir in self._dirs:
            size += dir.getSize()
        for file in self._files:
            size += file.getSize()

        return size

    def getFiles(self) -> list['File']:
        return self._files

    def getDirs(self) -> list['Dir']:
        return self._dirs

    def getDir(self, name: str) -> 'Dir':
        for dir in self._dirs:
            if dir.getName() == name:
                return dir
        return None

    def addDir(self, name: str) -> None:
        self._dirs.append(Dir(name, self))

    def addFile(self, name: str, size: int) -> None:
        self._files.append(File(name, size))

    def getChallengeSum(self) -> int:
        sum = self.getSize()
        if sum > 100000:
            sum = 0

        for dir in self._dirs:
            sum += dir.getChallengeSum()

        return sum

    def getSmallestDirsBiggerThan(self, min: int) -> list['Dir']:
        ls = list()
        if self.getSize() >= min:
            for dir in self._dirs:
                ls += dir.getSmallestDirsBiggerThan(min)
            if len(ls) == 0:
                ls.append(self)

        return ls
