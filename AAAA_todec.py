# -*- coding: utf-8 -*-

def main():
    # for i in range(1, 10000):
    #     print("{:3d}: {:06d}".format(i, aaa_to_hex(i)))
    print(aaa_to_hex(1000000))

def aaa_to_hex(n):
    if n > 5:
        n = (n - 6) % 3125 + 6
    return int('A' * n, 16) % 1000000

if __name__ == '__main__':
    main()
