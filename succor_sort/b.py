import time
from pprint import pprint as pp

def lineup(a, k, t, res):
    if k == 0:
        res.append(a)
        return
    i = 0
    while i + k + 1 < t:
        s = i
        e = i + k + 1
        i += 1
        if a[s] is not None or a[e] is not None:
            continue
        ta = a[:]
        # NOTE: no need filling number 
        ta[s] = k
        ta[e] = k
        lineup(ta, k - 1, t, res)

t = 11
a = [None for i in range(t * 2)]
res = []
lineup(a, t, len(a), res)
print(len(res))
print(len(list(set(res))))

