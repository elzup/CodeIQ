import time
from pprint import pprint as pp


def lineup(b, k):
    global l
    if k == 0:
        global c
        c += 1
        return
    i = 0
    while i + k + 1 < l:
        bt = b
        s = i
        e = i + k + 1
        i += 1
        if (bt >> s & 1) or (bt >> e & 1):
            continue
        # NOTE: no need filling number 
        bt |= (1 << s) | (1 << e)
        lineup(bt, k - 1)


start = time.time()

k = 11
c = 0
l = k * 2
lineup(0, k)
print(c)
print(str(time.time() - start) + "ms")

