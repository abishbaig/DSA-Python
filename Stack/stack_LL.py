class Node:
    def __init__(self, data: int, next: "Node" = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self):
        self.head: Node = None
        self.size: int = 0

    # T.C = O(1)
    def insertAtHead(self, val: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    # T.C = O(1)
    def __len__(self) -> int:
        return self.size

    # T.C = O(1)
    def deleteAtHead(self) -> int:
        if not self.head:
            print("Stack Underflow Error")
        else:
            tempNode: Node = self.head
            tempData = tempNode.data
            self.head = tempNode.next
            del tempNode

            self.size -= 1
            return tempData

    # T.C = O(1)
    def isEmpty(self) -> bool:
        if self.head:
            return False
        else:
            return True

    # T.C = O(1)
    def peekAtHead(self) -> int:
        if self.isEmpty():
            return self.head.data
        else:
            print("Stack Underflow Error")

    # T.C = O(1)
    def updateAtHead(self, newVal: int):
        if self.isEmpty():
            self.head.data = newVal
        else:
            print("List is not initialized")


def main():
    stack = Stack()
    stack.insertAtHead(1)
    stack.insertAtHead(2)
    stack.insertAtHead(3)
    stack.insertAtHead(4)

    while stack.isEmpty() != True:
        print(stack.deleteAtHead())


if __name__ == "__main__":
    main()
