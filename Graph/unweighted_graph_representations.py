from typing import List
from collections import defaultdict, deque


# T.C = O(N^2) - S.C = O(1)
def printEdgeLst(graphLst: List[List[int]], row: int, col: int):
    # for vertex in range(row):
    #     for neigbour in range(col):
    #         print(graphLst[vertex][neigbour], end=" -> ")
    #     print()

    for vertex, neighbours in graphLst:
        print(vertex, " -> ", neighbours)


# T.C = O(V) - S.C = O(V^2)
def makeAdjacencyMatrix(graphLst: List[List[int]], vertxNum: int) -> List[List[int]]:
    # Make an Matrix of vertxNum * vertxNum - n * n
    matrix: List[List[int]] = []
    for i in range(vertxNum):
        matrix.append([0] * vertxNum)

    # Assigning Edges
    for source, vertex in graphLst:
        # ! Assign Weights if present instead of 1 as it shows only a connection/edge
        matrix[source][vertex] = 1

        # ! In-case of undirected graph
        # matrix[vertex][source] = 1

    return matrix


# T.C = O(V^2) - S.C = O(1)
def printAdjMatrix(matrix: List[List[int]], vertxNum: int):
    for src in range(vertxNum):
        for vert in range(vertxNum):
            if matrix[src][vert] >= 1:
                print(src, "-> ", vert)


# T.C = O(V) - S.C = O(V + E)
def makeAdjLst(graphLst: List[List[int]]) -> defaultdict[list]:
    graphAdjLst: defaultdict[list] = defaultdict(list)

    # Preprocessing
    for src, vert in graphLst:
        graphAdjLst[src].append(vert)

    return graphAdjLst


# T.C = O(1) in average case - S.C = O(1)
def printAdjLst(graphAdjLst: defaultdict[list]):
    for src, vert in graphAdjLst.items():
        print(src, " -> ", vert)


# Nodes Representation
class GraphNode:
    def __init__(self, val: int):
        self.val: int = val
        self.neighbours: List["GraphNode"] = []

    def __str__(self):
        return str(self.val)

    def displayNeighbours(self):
        print(self, end=" -> ")
        neighbours: List[int] = [node.val for node in self.neighbours]
        print(neighbours)


def main():

    # 1. Edge List
    numOfVertices: int = 8
    graphEdgeLst: List[List[int]] = [
        [0, 1],
        [0, 3],
        [1, 2],
        [3, 4],
        [3, 6],
        [3, 7],
        [4, 2],
        [4, 5],
        [5, 2],
    ]

    # Printing Edge List
    # Rows = 9
    # Columns = 2
    # printEdgeLst(graphEdgeLst, 9, 2)

    # 2. Adjacency Matrix
    # adjMatrix: List[List[int]] = makeAdjacencyMatrix(graphEdgeLst, numOfVertices)
    # printAdjMatrix(adjMatrix, numOfVertices)

    # 3. Adjacency List
    # graphAdjLst: defaultdict[list] = makeAdjLst(graphEdgeLst)
    # printAdjLst(graphAdjLst)

    # 4. Node Representations
    node_0 = GraphNode(0)
    node_1 = GraphNode(1)
    node_2 = GraphNode(2)
    node_3 = GraphNode(3)
    node_4 = GraphNode(4)
    node_5 = GraphNode(5)
    node_6 = GraphNode(6)
    node_7 = GraphNode(7)

    # Adding Edges
    node_0.neighbours.extend([node_1, node_3])
    node_1.neighbours.extend([node_2])
    node_3.neighbours.extend([node_4, node_6, node_7])
    node_4.neighbours.extend([node_2, node_5])
    node_5.neighbours.extend([node_2])

    # Printing neighbours
    for src in [node_0, node_1, node_2, node_3, node_4, node_5, node_6, node_7]:
        src.displayNeighbours()


if __name__ == "__main__":
    main()
