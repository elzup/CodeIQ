import string
import math


def main():
    ns = list(map(int, input().split(',')))
    i = 10
    while 1:
        # print("i:", i)
        if all(is_palindrome(int2base(i, n)) for n in ns):
            print(i)
            break
        i += 1


def is_palindrome(n):
    # print('ck: ', str(n)[::-1], str(n))
    return str(n)[::-1] == str(n)


def int2base(a, b):
    return (''.join((string.digits + string.ascii_letters)[(a // b ** i) % b]
            for i in range(int(math.log(a, b)), -1, -1)))


if __name__ == '__main__':
    main()
