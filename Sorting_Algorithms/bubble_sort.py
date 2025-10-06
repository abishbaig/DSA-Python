import array as arr


# With Improvement to Check if Array already sorted
# T.C = O(N^2) - S.C = O(1)
def bubbleSort(arr: arr.array):
    n = len(arr)
    for i in range(n):
        swapped: bool = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If Swapping Didn't happen it means array is sorted so return Successfully in 1 Iteration only
        if not swapped:
            break


def main():
    arr1: arr.array = arr.array("i", [1, 2, 3, 5, 4])
    print(arr1)
    bubbleSort(arr1)
    print(arr1)


if __name__ == "__main__":
    main()
