import time
from pprint import pprint as pp


def lineup(a, k):
    global memo
    c = 0
    if k == 1:
        return len(a) == 3
    for s in range(len(a) - k - 1):
        e = s + k + 1
        if a[s] or a[e]:
            continue
        a[s] = a[e] = True
        ws = a.index(False)
        we = len(a) - a[::-1].index(False) - 1
        c += lineup(a[ws:we + 1], k - 1)
        a[s] = a[e] = False
    return c

start = time.time()

k = 11
l = k * 2
memo = {}
a = [False for i in range(k * 2)]
c = lineup(a, k)
print(c)

print(str(time.time() - start) + "ms")

