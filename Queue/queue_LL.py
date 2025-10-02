class Node:
    def __init__(self, data: int, next: "Node" = None, prev: "Node" = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.data)


class Queue:
    def __init__(self):
        self.front: Node = None
        self.rear: Node = None
        self.size: int = 0

    # T.C = O(1)
    def enqueue(self, val: int):
        newNode: Node = Node(val)
        if not self.front:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

        self.size += 1

    # T.C = O(1)
    def __len__(self) -> int:
        return self.size

    # T.C = O(1)
    def dequeue(self) -> int:
        if not self.front:
            print("Queue is Empty")
            return float("-inf")
        else:
            tempNode: Node = self.front
            tempData: int = tempNode.data
            self.front = tempNode.next
            tempNode.next = None
            if self.front != None:
                self.front.prev = None
            del tempNode

            self.size -= 1
            return tempData

    # T.C = O(1)
    def updateFront(self, newVal: int):
        if self.front == None:
            print("Queue is Empty")
        else:
            self.front.data = newVal

    # T.C = O(1)
    def updateRear(self, newVal: int):
        if self.front == None:
            print("Queue is Empty")
        else:
            self.rear.data = newVal

    # T.C = O(1)
    def isEmpty(self) -> bool:
        if self.front:
            return False
        else:
            return True

    # T.C = O(1)
    def peekFront(self) -> int:
        if self.isEmpty():
            print("Queue is Empty")
            return float("-inf")
        else:
            return self.front.data

    # T.C = O(1)
    def peekRear(self) -> int:
        if self.isEmpty():
            print("Queue is Empty")
            return float("-inf")
        else:
            return self.rear.data


def main():
    queue: Queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    while queue.isEmpty() != True:
        print(queue.dequeue())


if __name__ == "__main__":
    main()
