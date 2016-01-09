import sys


def calc_powpow(x, y, z):
    return x ** (y ** z)


class PowPowCompare:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def point(self, pp):
        if pp.z == self.z:
            if pp.y == self.y:
                return self.x
            return self.x ** (self.y / pp.y)
        return self.x ** (self.y ** (self.z / pp.z) ** pp.z / (pp.y ** pp.z))

if __name__ == '__main__':
    max_no = -1
    max_value = 0.0
    ppf = None
    lines = list(enumerate(sys.stdin))
    ps = []
    for no, line in lines[::-1]:
        x, y, z = map(float, line.split(","))
        ps += [PowPowCompare(x, y, z)]

    ps.sort(key=lambda x: x.point())
    print("%d" % (len(lines) - max_no - 1))
