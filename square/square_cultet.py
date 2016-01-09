# import time
import math


def main():
    for i in range(2, 10):
        print(i, sum(squares(1, i)))


def main2():
    a, b = map(int, input().split())
    # start = time.time()
    print(sum(squares(a, b)))
    # print(str((time.time() - start) * 1000) + "ms")


def squares(a, b):
    k = (b + a) * (b - a)
    # print(k)
    x, y = 2, 1
    ps = []
    t = 3
    while x > y:
        # print(x, y, t)
        if t > k:
            dy = max(1, int(- y + math.sqrt(y ** 2 + t - k)))
            t -= dy * (dy + 2 * y)
            y += dy
            continue
        if t == k:
            # print(">", x, y)
            ps += [x, y]
        # t += x * 2 + 1
        dx = max(1, int(- x + math.sqrt(x ** 2 - t + k)))
        t += dx * (dx + 2 * x)
        x += dx
    return ps

if __name__ == '__main__':
    main()
