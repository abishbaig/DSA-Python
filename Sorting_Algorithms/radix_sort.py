import array as arr
from typing import List


# T.C = O(N.k) [k = len(highest number of digits)]
# T.C = O(N) if k is less
# T.C = O(N^2) if k is high then N
# T.C = O(N log N) if k ~ log N


# S.C = O(K) [K = len(radixArray)]
def radixSort(arr: arr.array):
    # Find Max Array's Element
    maxElement: int = max(arr)

    # Initailzing an Radix Array with of Size: Range (0 - 9)
    # Each Index will contain its own individual array for storing numbers from actual array
    radixArray: List[List[int]] = [[], [], [], [], [], [], [], [], [], []]

    # Starting with Exponent = 1 then it will be multiplied by 10 after each iteration
    # Means: Ones, Tens, Hundreds, Thousands, ... [Logic]
    exponent: int = 1

    # A Max Element will always have higher number of digits so if it is divisibly by 0, it means there is no more digit to further explore
    while maxElement // exponent > 0:
        # Counting Sort Logic

        # Precomputing Step
        for i in range(len(arr)):
            # First Finding LSD (Least Significant Digit) to serve as index where the acutal value should be placed within Radix Array
            # Results = 0, For Number Digits: If the Digits of High Number still exits but the number itself has less digits
            radixIndex: int = (arr[i] // exponent) % 10
            radixArray[radixIndex].append(arr[i])

        # Bucket = List withing Radix Array's each index
        orgArrPtr: int = -1
        for bucket in radixArray:
            for indx in range(len(bucket)):
                arr[orgArrPtr := orgArrPtr + 1] = bucket[indx]

        # Clearing buckets for next pass
        for bucket in radixArray:
            bucket.clear()

        # Updating Exponent to validate next Digit
        exponent *= 10


def main():
    arr1: arr.array = arr.array("i", [7, 12, 9, 11, 3])
    print(arr1)
    radixSort(arr1)
    print(arr1)


if __name__ == "__main__":
    main()
