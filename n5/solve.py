# -*- coding: utf-8 -*-
import fileinput
import math


def main():
    # for line in range(180, 200):
    #     print(line)
    #     print("s", solve(int(line)))
    #     print("")
    for line in fileinput.input():
        print(solve(int(line)))


def solve(n):
    if (n <= 5):
        return n + 5 - 1
    k_shift = 5
    base = 10
    # 制限
    for k in range(2, 10):
        kn = f10(k)
        if (n <= k_shift + kn):
            break
        base = math.pow(10, k)
        k_shift += kn
    t = n - k_shift - 1
    # print("k", k)
    # print("ks", k_shift)
    # print("base", base)
    # print("t", t)
    # print("tk", t % k)
    return digit(t / k + base, t % k)


def f10(k):
    return 9 * math.pow(10, k - 1) * k


def digit(n, k):
    return int(str(int(n))[int(k)])


if __name__ == '__main__':
    main()
