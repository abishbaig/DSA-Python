from pathlib import Path
import sys

"""
- Add the DSA directory to Python path
- Path returns a Path Object
- __file__ returns the full path of current working directory
- .parent works like cd ..
- sys.path includes all directories where import should search for modules
"""

dsa_directory = Path(__file__).parent.parent
sys.path.append(str(dsa_directory))

from Linked_List.singly_LL import SinglyLL, Node


# T.C = O(n) - S.C = O(n)
def reverseList(node: Node):
    if not node:
        return
    reverseList(node.next)
    print(node)


def main():
    lst: SinglyLL = SinglyLL()
    lst.insertAtHead(1)
    lst.insertAtTail(2)
    lst.insertAtTail(3)
    lst.insertAtTail(4)

    reverseList(lst.head)


if __name__ == "__main__":
    main()
