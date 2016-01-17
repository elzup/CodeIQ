import sys
import re


class File:
    def __init__(self, name):
        self.name = name
        res = re.compile('(.*?)([0-9]*)\.(.*)$').match(name)
        if res:
            self.name_str = res.group(1)
            self.name_num = int(res.group(2))
            self.ext = res.group(3)

    def __lt__(self, other):
        if self.name_str != other.name_str:
            return self.name_str < other.name_str
        if self.name_num != other.name_num:
            return self.name_num < other.name_num
        return self.name < other.name

    def __gt__(self, other):
        return other.__lt__(self)

    def __str__(self):
        return self.name

files = []
for line in sys.stdin:
    files.append(File(line.strip()))

files.sort()
print("\n".join(map(str, files)))
