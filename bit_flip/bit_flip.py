def main():
    s, e = map(int,  input().split(','))
    print(count_bit_flip(range(s + 1, e)))


def count_bit_flip(li):
    return list(map(is_bit_flip, li)).count(True)


def is_bit_flip(n):
    return n == bit_flip(n)


def bit_flip(n):
    return int(bin(n)[2:][::-1], 2)


if __name__ == '__main__':
    main()
