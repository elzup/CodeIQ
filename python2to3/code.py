dividend, divisor = map(int, input().split())
try:
    print(dividend // divisor)
except ZeroDivisionError:
    print("ERR")
