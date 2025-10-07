from collections import defaultdict
from typing import List

"""
A: [(B, 1), (C, 2)]
B: [(D, 4)]
C: [(B, 3)]
D: [()]
"""

# Graph Implementation using Graph Node


class Graph:
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


def main():
    graph: Graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "B", 3)

    for nodes in ["A", "B", "C", "D"]:
        graph.printNeighbours(nodes)


if __name__ == "__main__":
    main()
