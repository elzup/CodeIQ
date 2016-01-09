import sys


def main():
    for line in list(map(lambda l: l.strip(), sys.stdin)):
        try:
            mn = MyNumber(line)
            if mn.has_check_digit():
                print(mn.check_digit_s())
            else:
                print(mn.generate_check_digit())
        except ValueError:
            print('Error')


class MyNumber:
    def __init__(self, s):
        if len(s) not in [11, 12]:
            raise ValueError
        try:
            int(s)
        except TypeError:
            raise ValueError
        self.check = None
        self.n = s
        if len(s) == 12:
            self.check = int(s[11])
            self.n = s[:11]

    def has_check_digit(self):
        return self.check is not None

    def check_digit_s(self):
        return ['NG', 'OK'][self.check_digit()]

    def check_digit(self):
        return self.check == self.calc_check_digit()

    def generate_check_digit(self):
        self.check = self.calc_check_digit()
        return self.check

    def calc_check_digit(self):
        ns = list(map(int, self.n))[::-1]
        t = sum(ns[i] * (i + 2) for i in range(6))
        t += sum(ns[i + 6] * (i + 2) for i in range(5))
        t %= 11
        return 0 if t <= 1 else 11 - t


if __name__ == '__main__':
    main()
