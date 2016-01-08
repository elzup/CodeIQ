import itertools
import time

for t in range(1, 6):
    start = time.time()
    seq = range(t) + range(t)
    print(t)
    print(seq)
    c = 0
    for p in list(set(itertools.permutations(seq))):
        if all(t - p[::-1].index(i) - p.index(i) == i for i in range(t)):
            print(p)
            c += 1
    print("c: " + str(c))
    print(str(time.time() - start) + "ms")
    print('')

