class TreeNode:
    def __init__(self, data: int):
        self.data: int = data
        self.left: "TreeNode" = None
        self.right: "TreeNode" = None
        self.height: int = 0

    def __str__(self):
        return str(self.data)


class AVL:
    def __init__(self):
        self.root: TreeNode = None

    # T.C = O(1) - S.C = O(1)
    def getHeight(self, node: TreeNode) -> int:
        if not node:
            return -1
        else:
            return node.height

    # T.C = O(1) - S.C = O(1)
    def getBalanceFactor(self, node: TreeNode) -> int:
        if not node:
            return 0
        else:
            return self.getHeight(node.right) - self.getHeight(node.left)

    # T.C = O(1) - S.C = O(1)
    def rotateRight(self, node: TreeNode) -> TreeNode:
        if node is None or node.left is None:
            return node
        print("Rotate Right on : ", node.data)
        # node: Node to Perform Rotation on
        # Assigning leftNodePointer -> Node's Left child which will be new parent node
        # Assigning leftNodeRightPointer -> Node's Left Child's Right Child Subtree if present which will be attached to Previous Parent Node's Left Side
        leftNodePointer: TreeNode = node.left
        leftNodeRightPointer: TreeNode = leftNodePointer.right

        leftNodePointer.right = node
        node.left = leftNodeRightPointer

        # Recalculating Updated Node's Heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        leftNodePointer.height = 1 + max(
            self.getHeight(leftNodePointer.left), self.getHeight(leftNodePointer.right)
        )

        # Return new Updated Parent Node
        return leftNodePointer

    # T.C = O(1) - S.C = O(1)
    def rotateLeft(self, node: TreeNode) -> TreeNode:
        if node is None or node.right is None:
            return node
        print("Rotate Left on : ", node.data)
        # node: Node to Perform Rotation on
        # Assigning rightNodePointer -> Node's Right child which will be new parent node
        # Assigning rightNodeleftPointer -> Node's Right Child's Left Child Subtree if present which will be attached to Previous Parent Node's Left Side

        rightNodePointer: TreeNode = node.right
        rightNodeLeftPointer: TreeNode = rightNodePointer.left

        rightNodePointer.left = node
        node.right = rightNodeLeftPointer

        # Recalculating Heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        rightNodePointer.height = 1 + max(
            self.getHeight(rightNodePointer.left),
            self.getHeight(rightNodePointer.right),
        )

        # Returning new Updated Parent Node
        return rightNodePointer

    def __balanceTree(self, node: TreeNode) -> TreeNode:
        if not node:
            return None
        # Updation of Node's Height and Calculating and Checking Balance Factor for Rotations
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        # Checking Balance Factor = H(Node.Right) - H(Node.Left)s
        balanceFactor = self.getBalanceFactor(node)

        # Checking Balance Factor and Performing Rotations on 4 Different Cases
        # Case 1: LL Case -> Perform Right Rotation as Tree is Left Heavy
        if balanceFactor < -1 and self.getBalanceFactor(node.left) <= 0:
            print("LL Case")
            return self.rotateRight(node)

        # Case 2: RR Case -> Perform Left Rotation as Tree is Right Heavy
        if balanceFactor > 1 and self.getBalanceFactor(node.right) >= 0:
            print("RR Case")
            return self.rotateLeft(node)

        # Case 3: LR Case -> First Perform Left Rotation on Node's Left Child then Perform Right Rotation on the Node
        if balanceFactor < -1 and self.getBalanceFactor(node.left) > 0:
            print("LR Case")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        # Case 4: RL Case -> First Perform Right Rotation on Node's Right Child then Perform Left Rotation on the Node
        if balanceFactor > 1 and self.getBalanceFactor(node.right) < 0:
            print("RL Case")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    # T.C = O(log N) - S.C = O(log N)
    def __insertNode(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return TreeNode(val)

        # Finding Value's Insertion Place in the tree
        if val < node.data:
            node.left = self.__insertNode(node.left, val)
        elif val > node.data:
            node.right = self.__insertNode(node.right, val)

        # Balancing Tree
        return self.__balanceTree(node)

    # Helper Function for Insertion
    def insertNode_AVL(self, val: int):
        self.root = self.__insertNode(self.root, val)

    # In-Order Successor Finding Function
    # T.C = O(H) - S.C = O(1)
    def minOrderValue(self, node: TreeNode) -> TreeNode:
        currNode: TreeNode = node
        while currNode.left != None:
            currNode = currNode.left
        return currNode

    # T.C = O(log N) - S.C = O(log N)
    def __deleteNode(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None

        # Finding Value in AVL
        if val < node.data:
            node.left = self.__deleteNode(node.left, val)
        elif val > node.data:
            node.right = self.__deleteNode(node.right, val)
        else:
            # Value Found
            # 3 Cases for Deletion

            # Case 1 & 2 : Node has 0 or 1 Child Node
            if node.left == None:
                tempNode: TreeNode = node.right
                node = None
                return tempNode
            elif node.right == None:
                tempNode: TreeNode = node.left
                node = None
                return tempNode

            # Case 3: Node has 2 Child Nodes
            # Update Node to Delete Data with Node's Right Subtree Smallest Value - Inorder Successor of Current Node
            # Delete Node in Right Subtree with the Updated Node's Value
            node.data = self.minOrderValue(node.right).data
            node.right = self.__deleteNode(node.right, node.data)

        # Balance Tree Before Returning the Node
        return self.__balanceTree(node)

    # Helper Function for Deletion
    def deleteNode_AVL(self, val: int):
        self.root = self.__deleteNode(self.root, val)

    # T.C = O(n) - S.C = O(n)
    def inOrderTraversal(self, node: TreeNode):
        if not node:
            return
        self.inOrderTraversal(node.left)
        print(node)
        self.inOrderTraversal(node.right)


def main():
    avlTree = AVL()
    print("Insertions")
    avlTree.insertNode_AVL(10)
    avlTree.insertNode_AVL(20)
    avlTree.insertNode_AVL(30)
    avlTree.insertNode_AVL(40)
    avlTree.insertNode_AVL(50)
    avlTree.inOrderTraversal(avlTree.root)
    print("------------------------------------")
    print("Deletion")
    avlTree.deleteNode_AVL(40)
    avlTree.inOrderTraversal(avlTree.root)


if __name__ == "__main__":
    main()
