import math


def main():
    a, n, s = input().split(',')
    a = int(a)
    n = int(n)
    print(progress_bar(a, n, s))


def progress_bar(a, n, s):
    if a < n:
        return 'invalid'
    return rate(a, n) * s


def rate(a, n):
    return math.floor(n * 100 / a)


if __name__ == '__main__':
    main()
