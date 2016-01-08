import itertools
import time

t = 11
start = time.time()
seq = range(t) + range(t)
print(t)
print(seq)
c = 0

for p in itertools.permutations(seq):
    if all(t - p[::-1].index(i) - p.index(i) == i for i in range(t)):
        print(p)
        c += 1
    if c > 100:
        break

print('c: ' + str(c))
print(str(time.time() - start) + "ms")
print('')
