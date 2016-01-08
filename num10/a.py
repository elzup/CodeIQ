# -*- coding: utf-8 -*-
def num_bit(num):
    return format(num, 'b').count("1")


def num_tenbit(num):
    return sum([num_bit(int(i)) for i in list(str(num))])


for i in range(1, 100):
    if num_bit(i) == num_tenbit(i):
        print(i)
        print(format(i, 'b'))
        print([num_bit(int(i)) for i in list(str(i))])
        print()
