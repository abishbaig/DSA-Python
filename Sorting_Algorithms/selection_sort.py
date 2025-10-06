import array as arr


# T.C = O(N^2) - S.C = O(1)
def selectionSort(arr: arr.array):
    n = len(arr)
    for i in range(n - 1):
        smallIndex: int = i
        for j in range(i, n):
            if arr[j] < arr[smallIndex]:
                smallIndex = j
        arr[i], arr[smallIndex] = arr[smallIndex], arr[i]


def main():
    arr1: arr.array = arr.array("i", [64, 34, 25, 12, 22, 11, 90, 5])
    print(arr1)
    selectionSort(arr1)
    print(arr1)


if __name__ == "__main__":
    main()
