import array as arr


# T.C = Average Case: O(N log N) and Worst Case: O(N^2) - S.C = O(N)
def quickSort(arr: arr.array, low: int, high: int):
    # Checking If Array's Range is Valid means have more than 1 or 0 Elements
    if low < high:
        # Finding Pivot Index at Each Division Step
        pivot_index: int = partition(arr, low, high)

        # Conquer Step
        # Left Sub-Array Sort
        quickSort(arr, low, pivot_index - 1)  # assumed_mid = pivot_index - 1

        # Right Sub-Array Sort
        quickSort(arr, pivot_index + 1, high)  # pivot_index+1 = mid+1


def partition(arr: arr.array, low: int, high: int) -> int:
    pivotElement: int = arr[low]  # Taking First Element as Pivot Element

    i: int = low
    j: int = high

    # "i" should find higher element than while it is less than the last index so don't go beyond array's bound
    # "j" should find lower or equal element than pivotElement while it is greater than the first index so don't go beyond array's bound

    while i < j:
        # Check 1: for "i" [i:->]
        while arr[i] <= pivotElement and i <= high - 1:
            i += 1

        # Check 2: for "j" [<-:j]
        while arr[j] > pivotElement and j >= low + 1:
            j -= 1

        # After Iterating if i'th index is less than j'th index it means arr[i] > arr[j] so swap should be happen
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[j] and arr[low] values to sort them as arr[low] = pivot_Element
    arr[low], arr[j] = arr[j], arr[low]
    # Should Return J as the new Pivot Index
    return j


def main():
    arr1: arr.array = arr.array("i", [64, 34, 25, 12, 22, 11, 90, 5])
    print(arr1)
    quickSort(arr1, 0, len(arr1) - 1)
    print(arr1)


if __name__ == "__main__":
    main()
