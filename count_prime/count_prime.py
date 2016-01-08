import sys
import math
# import time


m_i = 2
m_c = 0
m_primes = []


def main():
    ns = list(map(int, list(sys.stdin)))
    # start = time.time()
    for n in ns:
        print(count_prime(n))
    # print(str((time.time() - start) * 1000) + "ms")


def count_prime(n):
    global m_c, m_primes, m_i
    for i in range(m_i, n):
        if is_prime(i, m_primes):
            m_primes += [i]
            m_c += 1
        m_i = i + 1
    return m_c


def is_prime(n, primes):
    nf = math.sqrt(n)
    for i in primes:
        if i > nf:
            break
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
