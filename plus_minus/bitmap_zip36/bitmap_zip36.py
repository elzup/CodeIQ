import math
import string


def main():
    line = ''.join(input() for i in range(5))
    # print(line)
    bins = line.replace('.', '0').replace('#', '1')
    # print(bins)
    ints = int(bins, 2)
    # print(ints)
    res = to36(ints)
    print(res)


def to36(n):
    return int2base(n, 36)


def int2base(a, b):
    # print(math.log(a, b))
    # print(range(int(math.log(a, b)), -1, -1))
    # print([i for i in range(int(math.log(a, b)), -1, -1)])
    # print([(a // b ** i) for i in range(int(math.log(a, b)), -1, -1)])
    # print([(a // b ** i) % b for i in range(int(math.log(a, b)), -1, -1)])
    return (''.join((string.digits + string.ascii_letters)[(a // b ** i) % b]
            for i in range(int(math.log(a, b)), -1, -1)))


if __name__ == '__main__':
    main()
