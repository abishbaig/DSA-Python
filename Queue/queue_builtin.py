from collections import deque


def main():
    # Double Ended Queue - Like Double Linked List for faster Appending at both ends
    queue: deque = deque()

    # T.C = O(1)
    queue.append(1)
    queue.append(2)
    queue.append(3)

    # T.C = O(1)
    print(queue.popleft())

    # T.C = O(1)
    print("Queue's Front Data: ", queue[0])

    # T.C = O(1)
    print("Queue's Rear Data: ", queue[-1])


if __name__ == "__main__":
    main()
