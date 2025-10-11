from typing import Dict, List


# Top Down DP using Memo
# T.C = O(N) - S.C = O(N)
# Closure Function
def fib1(num: int) -> int:
    # Pre Storing the Results of 0th and 1st Fib num
    memo: Dict[int, int] = {0: 0, 1: 1}

    def findFib(x: int):
        # If the Result is already calculated simply return it without exhaustive re-calculation
        if x in memo:
            return memo[x]
        else:
            # Fibonacci Number Formula
            memo[x] = findFib(x - 1) + findFib(x - 2)
            return memo[x]

    return findFib(num)


# Bottom Up DP using Tabulation
# T.C = O(N) - S.C = O(N)
def fib2(num: int) -> int:
    if num <= 1:
        return num

    # Initialzing an Array of Size : Num+1 to Precompute and Return the Result of Num itself
    dp: List[int] = [0] * (num + 1)
    # Each Index will act as Position for a fib num
    dp[0] = 0
    dp[1] = 1

    # Precomputing Step
    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num]


# Constant Space Solution
# T.C = O(N) - S.C = O(1)
def fib3(num: int) -> int:
    if num <= 1:
        return num

    prev: int = 0
    curr: int = 1
    result: int = 0

    for _ in range(2, num + 1):
        result = prev + curr
        prev = curr
        curr = result
        # prev, curr = curr, prev + curr

    return result


# T.C = O(1) - S.C = O(1)
def fib4(num: int) -> int:
    golden_ration: int = (1 + (5**0.5)) / 2
    return int(round((golden_ration**num) / (5**0.5)))


def main():
    print(fib4(4))


if __name__ == "__main__":
    main()
