import sys

lines = list(map(lambda x: x.strip(), list(sys.stdin)))
s = int(lines.pop(0), 2)
for line in lines:
    sig = line[0]
    n = int(line[1:], 2)
    if sig == '|':
        s |= n
    elif sig == '&':
        s &= n
    else:
        s ^= n
print(s)
