from collections import deque
from typing import List


class TreeNode:
    def __init__(self, data: int):
        self.data: int = data
        self.left: "TreeNode" = None
        self.right: "TreeNode" = None

    def __str__(self):
        return str(self.data)


# Will Implement Complete Binary Tree Reqs: Left Node First fill then Right and fill level by level
class BinaryTree:
    def __init__(self):
        self.root = None

    # Using BFS - Level Order Filling Technique
    # T.C = O(n) - S.C = O(n)
    # Note T.C = O(n) as Height of Binary Tree i.e H<=n that is why O(n)
    def insertNode(self, val: int):
        newNode: TreeNode = TreeNode(val)
        # If root is null first fill root
        if not self.root:
            self.root = newNode
            return

        # Maintaining a Queue for Level Order Checking
        queue: deque = deque([self.root])
        while queue:
            # Pop Front Element from Queue and Check in left of it is Null insert there else Insert into Queue
            # Then Check in right of it is Null insert there else Insert into Queue
            currNode: TreeNode = queue.popleft()
            if not currNode.left:
                currNode.left = newNode
                return
            else:
                queue.append(currNode.left)
            if not currNode.right:
                currNode.right = newNode
                return
            else:
                queue.append(currNode.right)

    # Recursive DFS - PreOrder Traversal = T.C = O(n) - S.C = O(n)
    def __preOrderTraversal(self, node: TreeNode):
        if not node:
            return
        print(node)
        self.__preOrderTraversal(node.left)
        self.__preOrderTraversal(node.right)

    # Recursive DFS - InOrder Traversal = T.C = O(n) - S.C = O(n)
    def __inOrderTraversal(self, node: TreeNode):
        if not node:
            return
        self.__inOrderTraversal(node.left)
        print(node)
        self.__inOrderTraversal(node.right)

    # Recursive DFS - PostOrder Traversal = T.C = O(n) - S.C = O(n)
    # Note T.C = O(n) as Height of Binary Tree i.e H<=n that is why O(n)
    def __postOrderTraversal(self, node: TreeNode):
        if not node:
            return
        self.__postOrderTraversal(node.left)
        self.__postOrderTraversal(node.right)
        print(node)

    # Iterative DFS : T.C = O(n) - S.C = O(n)
    def __iterativeDFS(self):
        stack: List[int] = [self.root]

        while stack:
            node: TreeNode = stack.pop()
            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # BFS - Level Order Traversal: T.C = O(n) - S.C = O(n)
    def __bfs(self):
        queue: deque = deque([self.root])
        while queue:
            node: TreeNode = queue.popleft()
            print(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Simple Caller Function
    def traverseTree(self, traverseType: str = "inorder"):
        if traverseType.lower() == "preorder":
            self.__preOrderTraversal(self.root)
        elif traverseType.lower() == "postorder":
            self.__postOrderTraversal(self.root)
        elif traverseType.lower() == "iterative dfs":
            self.__iterativeDFS()
        elif traverseType.lower() == "bfs":
            self.__bfs()
        else:
            self.__inOrderTraversal(self.root)

    # Recursive DFS Approach
    # T.C = O(n) - S.C = O(n)
    def searchTree(self, node: TreeNode, key: int) -> bool:
        if not node:
            return False

        if node.data == key:
            return True

        return self.searchTree(node.left, key) or self.searchTree(node.right, key)

    # Recursive DFS Approach
    # T.C = O(n) - S.C = O(N)
    def updateTree(self, node: TreeNode, target: int, newVal: int) -> bool:
        if not node:
            return False

        if node.data == target:
            node.data = newVal
            return True

        return self.updateTree(node.left, target, newVal) or self.updateTree(
            node.right, target, newVal
        )

    # Same Logic with Modifications as Insertion of Node in BT
    # T.C = O(n) - S.C = O(n)
    def deleteNode(self, target: int) -> bool:
        if not self.root:
            return False

        queue: deque = deque([self.root])
        # Maintain 3 Vars to Store LastNode, Node to Delete and Parent of the Last node
        lastNode: TreeNode = None
        parentOf_Last: TreeNode = None
        nodeToDel: TreeNode = None

        while queue:
            lastNode = queue.popleft()
            # Node to Delete Found
            if lastNode.data == target:
                nodeToDel = lastNode
            if lastNode.left:
                # Checkig of LastNode.left's Parent
                parentOf_Last = lastNode
                queue.append(lastNode.left)
            if lastNode.right:
                # Checkig of LastNode.right's Parent
                parentOf_Last = lastNode
                queue.append(lastNode.right)

        # Checking if Node to Delete Exists
        if not nodeToDel:
            return False

        # Removing Node Logic by Replacing with Last Node in Deepest Right Node
        nodeToDel.data = lastNode.data

        # Remove Node
        if parentOf_Last:
            # If the Last Node is already a Right Node of Parent
            if parentOf_Last.right == lastNode:
                parentOf_Last.right = None
            else:
                parentOf_Last.left = None
        else:
            # Only Root Node Exits no anyother Parent
            self.root = None

        return True


def main():
    btree: BinaryTree = BinaryTree()

    for vals in [15, 10, 15, 20, 30, 40]:
        btree.insertNode(vals)

    # btree.traverseTree("bfs")
    # print(btree.updateTree(btree.root, 30, 45))
    btree.deleteNode(30)
    btree.traverseTree("bfs")


if __name__ == "__main__":
    main()
