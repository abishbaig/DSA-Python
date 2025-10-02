class Node:
    def __init__(self, data: int, next: "Node" = None, prev: "Node" = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.data)


class DoublyLL:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    # T.C = O(1)
    def insertAtHead(self, val: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head, self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    # T.C = O(1)
    def insertAtTail(self, val: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head, self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # T.C = O(n)
    def __len__(self) -> int:
        tempNode: Node = self.head
        count: int = 0
        while tempNode:
            count += 1
            tempNode = tempNode.next

        return count

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

    # T.C = O(1)
    def deleteAtHead(self):
        if not self.head:
            print("List is not Initialiazed")
        else:
            tempNode: Node = self.head
            self.head = tempNode.next
            del tempNode

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
    obj = DoublyLL()
    obj.insertAtHead(1)
    obj.insertAtTail(2)
    obj.insertAtAnyPos(3, 2)
    obj.traverseList()
    obj.updateListByPos(5, 3)
    obj.traverseList()


if __name__ == "__main__":
    main()
