# -*- coding: utf-8 -*-
from functools import reduce
import itertools
import re

# only check num filterd by rule3
def main():
    solve()

def solve(level=0):
    for element in itertools.permutations(map(str, range(10)), 10):
        n = int("".join(element))
        if check_rule(n):
            print(n)
            exit() # only one finish

def check_rule(n):
    return check_rule1(n) and check_rule2(n)

def check_rule1(n):
    return n % 2520 == 0

def check_rule2(n):
    return reduce(lambda a,b: a & b, [n % int(i) for i in split2(n)], True)

def split2(n):
    sn = str(n)
    return [i+j for (i, j) in zip(list(sn), sn[1::])]

if __name__ == '__main__':
    main()
