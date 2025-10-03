import array as arr


# Traditional Binary Search
# T.C = O(log n) - S.C = O(1)
def binarySearch1(arr: arr.array, key: int):
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = left + ((right - left) // 2)  # Logic to Prevent Integer Overflow
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1


# Conditional Binary Search - First Occurence of the Key
# T.C = O(log n) - S.C = O(1)
def binarySearch2(arr: arr.array, key: int):
    left: int = 0
    right: int = len(arr)
    index: int = -1

    while left <= right:
        mid: int = left + ((right - left) // 2)
        if arr[mid] == key:
            index = mid
            right = mid - 1
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return index


def main():
    # arr1: arr.array = arr.array("i",[1,2,3,4,5])
    # print(binarySearch1(arr1,9))
    arr2: arr.array = arr.array("i", [0, 0, 0, 1, 1])
    print(binarySearch2(arr2, 1))


if __name__ == "__main__":
    main()
