import array as arr


# Overall T.C = O(N log N) - S.C = O(N)
# T.C = O(log N) - S.C = O(1)
def mergeSort(arr: arr.array) -> arr.array:
    # If array's len is 1 or 0 It means array is subdivided to 1 Element, Simply Return
    if len(arr) <= 1:
        return arr

    # Dividing Step
    mid: int = len(arr) // 2
    leftHalf: "arr.array" = arr[
        :mid
    ]  # T.C = O(K) where 'K' is len(subarray) <= len(arr)
    rightHalf: "arr.array" = arr[
        mid:
    ]  # T.C = O(K) `` `` ``   ``  ``  ``  ``   ``  `` ``

    sortedLeftHalf: "arr.array" = mergeSort(leftHalf)
    sortedRightHalf: "arr.array" = mergeSort(rightHalf)

    # Conquer Step
    return merge(sortedLeftHalf, sortedRightHalf)


# T.C = O(N) - S.C = O(N)
def merge(leftSubArray, rightSubArray) -> arr.array:
    # Final Sorted Array in Each Recursive Call to Return
    resultArr: "arr.array" = []
    i: int = 0
    j: int = 0

    # Initializing 2 Pointers; One for Left subarray and second for Right One
    # Appending Values in Final Array in Ascending Order
    while i < len(leftSubArray) and j < len(rightSubArray):
        if leftSubArray[i] < rightSubArray[j]:
            resultArr.append(leftSubArray[i])
            i += 1
        else:
            resultArr.append(rightSubArray[j])
            j += 1

    # When Insertion is Completed then again Check if Both Arrays have Elements Left then Insert into array
    while i < len(leftSubArray):
        resultArr.append(leftSubArray[i])
        i += 1

    while j < len(rightSubArray):
        resultArr.append(rightSubArray[j])
        j += 1

    return resultArr


def main():
    arr1: arr.array = arr.array("i", [64, 34, 25, 12, 22, 11, 90, 5])
    print(arr1)
    arr1 = mergeSort(arr1)
    print(arr1)


if __name__ == "__main__":
    main()
