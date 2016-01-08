import sys


def main():
    nums = list(map(int, list(sys.stdin)))
    nums = list(map(abs, nums))
    print(len(nums) - len(list(set(nums))))


if __name__ == '__main__':
    main()
