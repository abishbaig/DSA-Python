from typing import List


# Variable Length Window
def findLongestSubstringLen(string: str) -> int:
    left: int = 0
    longest: int = 0
    sett: set = set()

    for right in range(len(string)):
        while string[right] in sett:
            sett.remove(string[left])  # Constant Time Operation - O(1)
            left += 1  # Moving Left when a Same Var Encountered in set

        # Finding Window Lenght
        windw_len: int = (right - left) + 1
        # Updating Longest Substring Len
        longest = max(longest, windw_len)
        # Appending String Char in set
        sett.add(string[right])

    return longest


# Fixed Length Window
def maxAvgSubarray(arr: List[int], k: int) -> float:
    max_avg: float = 0

    cur_sum: float = 0

    for i in range(k):
        cur_sum += arr[i]

    max_avg = cur_sum / k

    for i in range(k, len(arr)):
        cur_sum += arr[i]
        cur_sum -= arr[i - k]

        avg: float = cur_sum / k
        max_avg = max(max_avg, avg)

    return max_avg


def main():
    # string: str = "pwwkew"
    # print(findLongestSubstringLen(string))
    print(maxAvgSubarray([1, 2, 0, -1], 3))


if __name__ == "__main__":
    main()
