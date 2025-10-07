from typing import List
from collections import defaultdict, deque


# T.C = O(V) - S.C = O(V + E)
def makeAdjLst(graphLst: List[List[int]]) -> defaultdict[list]:
    graphAdjLst: defaultdict[list] = defaultdict(list)

    # Preprocessing
    for src, vert in graphLst:
        graphAdjLst[src].append(vert)
        # ! For Undirected Graph below line
        graphAdjLst[vert].append(src)

    return graphAdjLst


# T.C = O(1) in average case - S.C = O(1)
def printAdjLst(graphAdjLst: defaultdict[list]):
    for src, vert in graphAdjLst.items():
        print(src, " -> ", vert)


# T.C = O(V+E) - S.C = O(V+E)
def recursiveDFS(sourceNode: int, graphAdjLst: defaultdict[list], visitedNodes: set):
    print(sourceNode)

    # Check Further Neighbours and add in call stack depth-wise if it is not visited
    # IF not visited add in visitednodes set and search for neighbours of that neighbour
    for neighbr in graphAdjLst[sourceNode]:
        if neighbr not in visitedNodes:
            visitedNodes.add(neighbr)
            recursiveDFS(neighbr, graphAdjLst, visitedNodes)


# T.C = O(V+E) - S.C = O(V+E)
def bfs(sourceNode: int, graphAdjLst: defaultdict[list]):
    visitedNodes: set = set()
    queue: deque = deque([sourceNode])
    visitedNodes.add(sourceNode)

    # While queue is not empty
    # Dequeue an node and print it
    # Check if its neighbours are not visited add them in the visitedSet and also in queue
    while queue:
        node = queue.popleft()
        print(node)
        for neighbour in graphAdjLst[node]:
            if neighbour not in visitedNodes:
                visitedNodes.add(neighbour)
                queue.append(neighbour)


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

    # 3. Adjacency List
    graphAdjLst: defaultdict[list] = makeAdjLst(graphEdgeLst)
    # printAdjLst(graphAdjLst)

    # Recursive DFS
    visitedSet: set = set()
    sourceNode: int = 0
    visitedSet.add(sourceNode)
    # recursiveDFS(sourceNode, graphAdjLst, visitedSet)

    # BFS
    bfs(0, graphAdjLst)


if __name__ == "__main__":
    main()
