# T.C = O(n) - S.C = O(1)
def reverseNumber(num: int) -> int:
    revNum: int = 0
    while num != 0:
        revNum = (revNum * 10) + (num % 10)
        num //= 10
    return revNum


def main():
    num: int = 1234
    print(reverseNumber(num))


if __name__ == "__main__":
    main()
