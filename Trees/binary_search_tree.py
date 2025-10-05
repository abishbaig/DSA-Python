class TreeNode:
    def __init__(self, data: int):
        self.data: int = data
        self.left: "TreeNode" = None
        self.right: "TreeNode" = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    # Inorder Traversal of BST always gives Ascending Order Values
    # T.C = O(n) - S.C = O(n)
    def inOrderTraversal(self, node: TreeNode):
        if not node:
            return
        self.inOrderTraversal(node.left)
        print(node)
        self.inOrderTraversal(node.right)

    # T.C = Best Case/Average Case - O(log n) and Worst Case = O(h)
    # S.C = Best Case/Average Case - O(log n) and Worst Case = O(h)
    # All nodes in the BST are unique, so in case we find the same value as the one we want to insert, we do nothing.
    def __insertNode(self, node: TreeNode, val: int):
        if not node:
            return TreeNode(val)
        else:
            if val < node.data:
                node.left = self.__insertNode(node.left, val)
            elif val > node.data:
                node.right = self.__insertNode(node.right, val)
        return node

    # Helper Function for Insertion
    def insertNode_BST(self, val: int):
        self.root = self.__insertNode(self.root, val)

    # T.C = Best Case/Average Case - O(log n) and Worst Case = O(h)
    # S.C = Best Case/Average Case - O(log n) and Worst Case = O(h)
    def __searchNode(self, node: TreeNode, target: int) -> bool:
        if not node:
            return False
        else:
            if target == node.data:
                return True
            elif target < node.data:
                return self.__searchNode(node.left, target)
            elif target > node.data:
                return self.__searchNode(node.right, target)

    # Helper Function for Searching
    def searchNode_BST(self, target: int):
        print(self.__searchNode(self.root, target))

    # MinOrderValue - Inorder Successor
    # T.C = O(node's left_subtree height/ node_left_H)
    # S.C = O(1)
    def minOrderValue(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        else:
            currNode: TreeNode = node
            while currNode.left != None:
                currNode = currNode.left
            return currNode

    # T.C = O(log N) but Worst = O(H)
    # S.C = O(log N) but Worst = O(H)
    def __deleteNode(self, node: TreeNode, target: int) -> TreeNode:
        if not node:
            return None

        if target < node.data:
            node.left = self.__deleteNode(node.left, target)
        elif target > node.data:
            node.right = self.__deleteNode(node.right, target)

        # If Node's Value Found

        # 3 Cases
        # Case 1: If Node to Delete is Leaf Node
        # Case 2: If Node to Delete has Only 1 Child Node
        else:
            if node.left == None:
                tempNode: TreeNode = node.right
                node = None
                return tempNode
            elif node.right == None:
                tempNode: TreeNode = node.left
                node = None
                return tempNode

            # Case 3: If Node to Delete has 2 Childrens Left and Right Both
            node.data = self.minOrderValue(node.right).data
            node.right = self.__deleteNode(node.right, node.data)

        return node

    # Helper Function for Node Deletion
    def deleteNode_BST(self, target: int):
        self.root = self.__deleteNode(self.root, target)


"""
                 10
                /  \\ 
               5    20
              / \\ 
             3   7
"""


def main():
    bst: BST = BST()
    bst.insertNode_BST(10)
    bst.insertNode_BST(5)
    bst.insertNode_BST(20)
    bst.insertNode_BST(3)
    bst.insertNode_BST(7)

    bst.deleteNode_BST(10)
    bst.inOrderTraversal(bst.root)
    # bst.searchNode_BST(90)
    # print(bst.minOrderValue(bst.root).data)


if __name__ == "__main__":
    main()
