# Solve any Problem (Usually where sorting factor is involved) in T.C = O(N)
# Example Problem : Squares of Numbers and Sort then reverse
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
from typing import List


# T.C = O(N) - S.C = O(N)
def squareOfNums(lst: List[int]) -> List[int]:
    result = []
    left: int = 0
    right: int = len(lst) - 1

    while left <= right:
        # First Sorting the entire list in Descending Order than will reverse it
        if abs(lst[left]) > abs(lst[right]):
            result.append(lst[left] ** 2)  # Appending after Squaring
            left += 1
        else:
            result.append(lst[right] ** 2)  # Appending after Squaring
            right -= 1

    result.reverse()  # In-place Reversing - T.C = O(N) , S.C = O(1)
    return result


def main():
    lst: List[int] = [-4, -1, 0, 3, 10]
    lst = squareOfNums(lst)
    print(lst)


if __name__ == "__main__":
    main()
