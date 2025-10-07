from typing import List
from collections import defaultdict


# T.C = O(N^2) - S.C = O(1)
def printEdgeLst(graphLst: List[List[int]]):
    for edge in graphLst:
        if len(edge) >= 3:
            # Extracting Source Vertex and Weight from the List of Ints within a List
            src, vertx, weigh = edge[0], edge[1], edge[2]
        else:
            src, vertx, weigh = edge[0], edge[1], edge[2]
        print(f"{src} -> {vertx} (W={weigh})")


# T.C = O(V) - S.C = O(V^2)
def makeAdjacencyMatrix(graphLst: List[List[int]], vertxNum: int) -> List[List[int]]:
    # Make an Matrix of vertxNum * vertxNum - n * n
    matrix: List[List[int]] = []
    for _ in range(vertxNum):
        matrix.append([0] * vertxNum)

    # Assigning Edges
    for edge in graphLst:
        # ! Assign Weights if present instead of 1 as it shows only a connection/edge
        if len(edge) >= 3:
            # Extracting Source Vertex and Weight from the List of Ints within a List
            src, vertx, weigh = edge[0], edge[1], edge[2]
        else:
            src, vertx, weigh = edge[0], edge[1], edge[2]

        # Making Connections with Weights
        matrix[src][vertx] = weigh

        # ! In-case of undirected graph
        # matrix[vertex][source] = 1

    return matrix


# T.C = O(V^2) - S.C = O(1)
def printAdjMatrix(matrix: List[List[int]], vertxNum: int):
    for src in range(vertxNum):
        for vert in range(vertxNum):
            weight: int = matrix[src][vert]
            if weight != 0:
                print(f"{src} -> {vert} (W={weight})")


# T.C = O(V) - S.C = O(V + E)
def makeAdjLst(graphLst: List[List[int]]) -> defaultdict[List[tuple]]:
    graphAdjLst: defaultdict[list] = defaultdict(list)

    # Preprocessing
    for src, vert, weight in graphLst:
        graphAdjLst[src].append((vert, weight))

    return graphAdjLst


# T.C = O(N) - S.C = O(1)
def printAdjLst(graphAdjLst: defaultdict[List[tuple]]):
    for src, neighbourLst in graphAdjLst.items():
        print(f"{src} -> {[f"{vert}, (W={weigh})" for vert, weigh in neighbourLst]}")


# Nodes Representation
class GraphNode:
    def __init__(self, val: int):
        self.val: int = val
        self.neighbours: List[tuple["GraphNode", int]] = []

    def __str__(self):
        return str(self.val)

    def displayNeighbours(self):
        print(self, end=" -> ")
        neighbours: List[tuple[int, int]] = [
            (node.val, weigh) for node, weigh in self.neighbours
        ]
        print(neighbours)


def main():
    # --------------------------------------------- Weighted Graph Implementations ------------------------------------------
    # [source, vertex, weight]  -> Default Weight = 1
    # ----------------------------------
    # 1. Edge List
    numOfVertices: int = 8
    graphEdgeLst: List[List[int]] = [
        [0, 1, 4],
        [0, 3, 3],
        [1, 2, 2],
        [3, 4, 1],
        [3, 6, 3],
        [3, 7, 2],
        [4, 2, 9],
        [4, 5, 1],
        [5, 2, 7],
    ]

    # Printing Edge List
    # Rows = 9
    # Columns = 2
    # printEdgeLst(graphEdgeLst)

    # 2. Adjacency Matrix
    # adjMatrix: List[List[int]] = makeAdjacencyMatrix(graphEdgeLst, numOfVertices)
    # printAdjMatrix(adjMatrix, numOfVertices)

    # 3. Adjacency List
    # graphAdjLst: defaultdict[List[tuple]] = makeAdjLst(graphEdgeLst)
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

    # # Adding Edges
    node_0.neighbours.extend([(node_1, 4), (node_3, 3)])
    node_1.neighbours.extend([(node_2, 2)])
    node_3.neighbours.extend([(node_4, 1), (node_6, 3), (node_7, 2)])
    node_4.neighbours.extend([(node_2, 9), (node_5, 1)])
    node_5.neighbours.extend([(node_2, 7)])

    # # Printing neighbours
    for src in [node_0, node_1, node_2, node_3, node_4, node_5, node_6, node_7]:
        src.displayNeighbours()


if __name__ == "__main__":
    main()
