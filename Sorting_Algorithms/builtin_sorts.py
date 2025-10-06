from typing import List


def main():
    lst1: List[int] = [7, 12, 9, 11, 3]
    # T.C = O(N log N) - S.C = O(1) -> In-place sorting
    lst1.sort()
    print(lst1)

    lst2: List[int] = [64, 34, 25, 12, 22, 11, 90, 5]
    # T.C = O(N log N) - S.C = O(N) -> Returns a New Array
    lst2 = sorted(lst2)
    print(lst2)

    # Sorting List containing another Data Structure like tuples
    tupList: List[tuple] = [(2, 1), (3, 4), (1, 6)]
    sortedTupList: List[tuple] = sorted(tupList, key=lambda tup: tup[0])
    print(sortedTupList)


if __name__ == "__main__":
    main()
