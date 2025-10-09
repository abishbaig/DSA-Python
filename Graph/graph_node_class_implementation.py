from collections import defaultdict
from typing import List

"""
A: [(B, 1), (C, 2)]
B: [(D, 4)]
C: [(B, 3)]
D: [()]
"""

# -----------------------------------------------------------------------------------------------------
# Graph Implementation using Array/List with Dictionary
# -----------------------------------------------------------------------------------------------------


class Graph_1:
    def __init__(self):
        # A Default Dictionary to automatically making a defautl empty list for every node
        self.graphAdjLst: defaultdict[List[tuple]] = defaultdict(list)
        self.size = 0

    def add_vertex(self, source: str):
        if source in self.graphAdjLst:
            return
        self.graphAdjLst[source] = []
        self.size += 1

    def add_edge(
        self, source: str, destination: str, weight: int, directed: bool = True
    ):
        # Ensuring vertices exist and updating graph size correctly
        if source not in self.graphAdjLst:
            self.add_vertex(source)
        if destination not in self.graphAdjLst:
            self.add_vertex(destination)

        # Avoiding duplicate edges
        for dest, w in self.graphAdjLst[source]:
            if dest == destination:
                return

        self.graphAdjLst[source].append((destination, weight))
        if not directed:
            self.graphAdjLst[destination].append((source, weight))

    def printNeighbours(self, vertex: str):
        if vertex not in self.graphAdjLst:
            print(f"{vertex} not present in graph")
            return
        neighbours = self.graphAdjLst[vertex]
        print(f"{vertex} -> {neighbours}")


# -----------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------
# Graph Implementation using Linked List with Dictionary
# -----------------------------------------------------------------------------------------------------
class GraphNode:
    def __init__(self, val: str):
        self.val: str = val
        self.adjacentNode: "GraphNode" = None

    def add_neighbours(self, vertx: "GraphNode"):
        if self.adjacentNode == None:
            self.adjacentNode = vertx
            return
        currNode = self.adjacentNode
        while currNode.adjacentNode != None:
            currNode = currNode.adjacentNode
        currNode.adjacentNode = vertx
        vertx.adjacentNode = None

    def __str__(self):
        return str(self.val)

    def print_neighbours(self):
        print(self.val, end=" -> ")
        currNode = self.adjacentNode
        while currNode != None:
            print(currNode, end=", ")
            currNode = currNode.adjacentNode
        print()


class Graph_2:
    def __init__(self):
        self.graphAdjLst: List[GraphNode] = []
        self.size = 0

    def add_vertex(self, source: GraphNode):
        if source not in self.graphAdjLst:
            self.graphAdjLst.append(source)
            self.size += 1

    def add_edge(self, source: GraphNode, destination: GraphNode):
        if source not in self.graphAdjLst:
            self.add_vertex(source)
        if destination not in self.graphAdjLst:
            self.add_vertex(destination)
        for i in range(self.size):
            if self.graphAdjLst[i] == source:
                self.graphAdjLst[i].add_neighbours(destination)
                break

    def printGraph(self):
        for i in range(self.size):
            self.graphAdjLst[i].print_neighbours()

    def dfs(self, source: "GraphNode"):
        visited = set()
        visited.add(source.val)
        stack = [source]
        while stack:
            node = stack.pop()
            print(node)
            adjNodes = node.adjacentNode
            while adjNodes != None:
                if adjNodes.val not in visited:
                    visited.add(adjNodes.val)
                    stack.append(adjNodes)
                adjNodes = adjNodes.adjacentNode


# -----------------------------------------------------------------------------------------------------


def main():

    a_N1 = GraphNode("A")
    b_N1 = GraphNode("B")
    c_N1 = GraphNode("C")
    d_N1 = GraphNode("D")

    lstGraph: Graph_2 = Graph_2()
    lstGraph.add_edge(a_N1, b_N1)
    lstGraph.add_edge(a_N1, c_N1)
    lstGraph.add_edge(b_N1, c_N1)
    lstGraph.add_edge(c_N1, d_N1)

    lstGraph.printGraph()


if __name__ == "__main__":
    main()
