class Node:
    def __init__(self, data: int, next: "Node" = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self):
        self.top: Node = None
        self.size: int = 0

    # T.C = O(1)
    def push(self, val: int):
        newNode: Node = Node(val)
        if not self.top:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

        self.size += 1

    # T.C = O(1)
    def __len__(self) -> int:
        return self.size

    # T.C = O(1)
    def pop(self) -> int:
        if not self.top:
            print("Stack Underflow Error")
            return float("-inf")
        else:
            tempNode: Node = self.top
            tempData = tempNode.data
            self.top = tempNode.next
            del tempNode

            self.size -= 1
            return tempData

    # T.C = O(1)
    def isEmpty(self) -> bool:
        if self.top:
            return False
        else:
            return True

    # T.C = O(1)
    def peek(self) -> int:
        if self.isEmpty():
            return self.top.data
        else:
            print("Stack Underflow Error")
            return float("-inf")

    # T.C = O(1)
    def updateAtTop(self, newVal: int):
        if self.isEmpty():
            self.top.data = newVal
        else:
            print("List is not initialized")


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    while stack.isEmpty() != True:
        print(stack.pop())


if __name__ == "__main__":
    main()
