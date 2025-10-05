import heapq
from typing import List

"""
           4                        0
          /  \\                    / \\
         3    2        --->       1    2
        / \\                     / \\
       1    0                   4    3
"""


# T.C = O(N log N) -  S.C = O(n)
def heapSort(heapArr: heapq) -> List[int]:
    if len(heapArr) <= 0:
        return []

    # Initailzing an Array of Size Heap Array where each Element by Default will be Zero
    lst: List[int] = [0] * len(heapArr)

    # Poping Each Heap Element - O(log N) for N Times = So Total Time Complexity = O(N log N)
    for i in range(len(heapArr)):
        lst[i] = heapq.heappop(heapArr)

    return lst


def main():

    # Build Heap using Heapify - Min Heap By Default
    # T.C = O(n) - S.C = O(1)
    heap: List[int] = [4, 3, 2, 1, 0]
    heapq.heapify(heap)

    # Heap Push
    # T.C = O(log N) - S.C = O(1)
    heapq.heappush(heap, -1)

    # Heap Pop - Extract Min
    # T.C = O(log N) - S.C = O(1)
    # print(heapq.heappop(heap))

    # print(heap)

    # Heap Sort
    # print(heapSort(heap))

    # Peek at Root Element - Min Value
    print(heap[0])

    """
    # Max Heap

    B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
    n = len(B)
    
    for i in range(n):
      B[i] = -B[i]
    
    heapq.heapify(B)

    largest = -heapq.heappop(B)
    heapq.heappush(B, -7) # Insert 7 into max heap

    # Build heap from scratch - Time: O(n log n)

    C = [-5, 4, 2, 1, 7, 0, 3]
    
    heap = []
    
    for x in C:
      heapq.heappush(heap, x)
      print(heap, len(heap)) # Check size of heap
    """


if __name__ == "__main__":
    main()
