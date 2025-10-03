# T.C = O(2^n) - S.C = O(n)
# Fail to find large numbers (even num = 100) sequence due to extensive computation power it demands
def fib(num: int) -> int:
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


def main():
    print(fib(5))


if __name__ == "__main__":
    main()
