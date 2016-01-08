# -*- coding: utf-8 -*-
import fileinput

n = 0
swap_list = []
for line in fileinput.input():
    pos = []
    qs = line.split(',')
    if not n:
        n = len(qs)
    for i, v in enumerate(map(int, qs)):
        if v:
            pos.append(i)
    swap_list.append(pos)

# print(swap_list)

# 縦棒は横線候補数 + 1個
wires = list(range(1, n + 2))
for qs in swap_list[::-1]:
    # swap
    for q in qs:
        wires[q], wires[q + 1] = wires[q + 1], wires[q]
        # print(q, wires)

print(",".join(map(str, wires)))
