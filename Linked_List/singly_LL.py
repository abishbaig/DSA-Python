class Node:
    def __init__(self, data: int, next: "Node" = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class SinglyLL:
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

    # T.C = O(n)
    def insertAtTail(self, val: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head = newNode
        else:
            tempNode: Node = self.head
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = newNode

        self.size += 1

    # T.C = O(1)
    def __len__(self) -> int:
        return self.size

    # T.C = O(n)
    def insertAtAnyPos(self, val: int, pos: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head = newNode
        elif pos > len(self):
            self.insertAtTail(val)
        else:
            # Using Slow Fast Pointer
            currNode: Node = self.head
            prevNode: Node = None

            for _ in range(1, pos):
                prevNode = currNode
                currNode = currNode.next

            prevNode.next = newNode
            newNode.next = currNode

        self.size += 1

    # T.C = O(1)
    def deleteAtHead(self):
        if not self.head:
            print("List is not Initialiazed")
        else:
            tempNode: Node = self.head
            self.head = tempNode.next
            del tempNode

            self.size -= 1

    # T.C = O(n)
    def deleteAtTail(self):
        if not self.head:
            print("List is not Initialiazed")
        else:
            currNode: Node = self.head
            prevNode: Node = None
            while currNode.next != None:
                prevNode = currNode
                currNode = currNode.next

            prevNode.next = None
            del currNode

            self.size -= 1

    # T.C = O(n)
    def deleteAtAnyPos(self, pos: int):
        if not self.head:
            print("List is not Initialiazed")
        elif pos <= 1:
            self.deleteAtHead()
        elif pos > len(self):
            self.deleteAtTail()
        else:
            currNode: Node = self.head
            prevNode: Node = None
            for _ in range(1, pos):
                prevNode = currNode
                currNode = currNode.next

            prevNode.next = currNode.next
            currNode.next = None
            del currNode

            self.size -= 1

    # T.C = O(n)
    def updateListByValue(self, newVal: int, prevVal: int):
        if self.head == None:
            print("List is not initialized")
        else:
            currNode: Node = self.head
            while currNode:
                if currNode.data == prevVal:
                    currNode.data = newVal
                    print("Updated Prev Value with New Value")
                    break
                currNode = currNode.next
            else:
                print("Value not Found")

    # T.C = O(n)
    def updateListByPos(self, newVal: int, pos: int):
        if self.head == None:
            print("List is not initialized")
        else:
            if len(self) < pos < 1:
                print("Position not Found")
            else:
                currNode: Node = self.head
                for _ in range(1, pos):
                    currNode = currNode.next
                currNode.data = newVal
                print("Updated Position Value with New Value")

    # T.C = O(n)
    def traverseList(self):
        tempNode: Node = self.head
        while tempNode:
            print(tempNode.data, end=" -> ")
            tempNode = tempNode.next
        print()


def main():
    obj = SinglyLL()
    obj.insertAtHead(1)
    obj.insertAtTail(2)
    obj.insertAtAnyPos(3, 2)
    obj.traverseList()
    obj.updateListByPos(5, 3)
    obj.traverseList()
    # print(len(obj))


if __name__ == "__main__":
    main()
