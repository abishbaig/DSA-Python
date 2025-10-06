import array as arr


# T.C = O(k+N) ~ k<=N so O(N) - S.C = O(K) [k = Max Element in Array]
def countingSort(arr: arr.array):
    # Find Max Array's Element
    maxElement: int = max(arr)

    # Initailzing an Frequency List of Size: len(maxElement+1)
    freqArray: "arr.array" = [0] * (maxElement + 1)

    # Precomputation Step : O(N)
    for i in range(len(arr)):
        freqArray[arr[i]] += 1

    # Sorting the Original Array
    orgArrCount: int = -1  # Starting with -1 due to pre-increment warlus operator usage
    # This Time Complexity is not O(N^2) due to Nested Loop
    # We are Iterating for O(K) Times and and in each time we are just decrement the frequency value not iterating the array itself
    for i in range(len(freqArray)):
        while freqArray[i] > 0:
            arr[orgArrCount := orgArrCount + 1] = i
            freqArray[i] -= 1


def main():
    arr1: arr.array = arr.array("i", [7, 12, 9, 11, 3])
    print(arr1)
    countingSort(arr1)
    print(arr1)


if __name__ == "__main__":
    main()
