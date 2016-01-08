def from_redix(num, b):
    n = 0
    numlist = list(num);
    while (numlist):
        n *= b
        n += int(numlist.pop(0))
    return n

def to_redix(n, b):
    if (int(n / b)):
        return to_redix(int(n/b), b) + str(n%b)
    return str(n%b)

# a, b = input(), input()
a, b = '18', '86'

for i in range(12, 30):
    n = from_redix('10', i) + from_redix('11', i)
    print(to_redix(n, i))
