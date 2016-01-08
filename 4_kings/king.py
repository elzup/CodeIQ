
def main():
    key, value = input().split(',')
    func = {
        'HelloWorld': hello,
        'FizzBuzz': fizz_buzz,
        'Prime': nth_prime,
        'Fibonacci': fibonacci
    }[key]
    print(func(int(value)))


# === HelloWorld ===
def hello(n):
    return 'HelloWorld' * n


# === FizzBuzz ===
def fizz_buzz(n):
    return ((not(n % 3)) * 'Fizz' + (not (n % 5)) * 'Buzz') or n


# === Prime ===
def nth_prime(n):
    primes = [2]
    c = 1
    i = 2
    while True:
        if c == n:
            return i
        i += 1
        if is_prime(i, primes):
            primes += [i]
            c += 1


def is_prime(n, primes):
    return all(n % i != 0 for i in primes)


# === Fibonacci ===
def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    main()
