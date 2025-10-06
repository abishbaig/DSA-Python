import array as arr


# T.C = O(N^2) - S.C = O(1)
def insertionSort(arr: arr.array):
    n = len(arr)
    for i in range(
        1, n
    ):  # Started with 1 because we assume that the First Index is Already Sorted
        for prev in range(
            i, 0, -1
        ):  # Starting from ith index and going to till start of sorted array
            if arr[prev - 1] > arr[prev]:
                arr[prev - 1], arr[prev] = arr[prev], arr[prev - 1]
            else:
                break


def main():
    arr1: arr.array = arr.array("i", [64, 34, 25, 12, 22, 11, 90, 5])
    print(arr1)
    insertionSort(arr1)
    print(arr1)


if __name__ == "__main__":
    main()
