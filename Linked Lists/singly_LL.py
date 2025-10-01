
class Node:
    def __init__(self, data: int, next: "Node" = None):
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        return str(self.data)
    
class SinglyLL:
    def __init__(self):
        self.head: Node = None
    
    # T.C = O(1)
    def insertAtHead(self, val: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

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
    
    def __len__(self) -> int:
        tempNode: Node = self.head
        count: int = 0
        while tempNode:
            count += 1
            tempNode = tempNode.next

        return count


    # T.C = O(n)
    def insertAtAnyPos(self,val: int, pos: int):
        newNode: Node = Node(val)
        if not self.head:
            self.head = newNode
        elif pos > len(self):
            self.insertAtTail(val)
        else:
            # Using Slow Fast Pointer
            currNode: Node = self.head
            prevNode: Node = None

            for i in range(1,pos):
                prevNode = currNode
                currNode = currNode.next
            
            prevNode.next = newNode
            newNode.next = currNode

    # T.C = O(n)
    def traverseList(self):
        tempNode: Node = self.head
        while tempNode:
            print(tempNode.data,end=" -> ")
            tempNode = tempNode.next

def main():
    obj = SinglyLL()
    obj.insertAtHead(1)
    obj.insertAtTail(2)
    obj.insertAtAnyPos(3,2)
    obj.traverseList()


if __name__=="__main__":
    main()
            
                




            
        