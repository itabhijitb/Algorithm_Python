from typing import *
import logging
logging.basicConfig(level=logging.WARN)


class Graph:
    def __init__(self, size, edges):
        self.edges = {}
        self.nodes = {}
        self.zero_indegree = []
        for edge in edges:
            u, v = edge
            self.edges.setdefault(v, []).append(u)
        self.nodes = {u: 0 for u in range(size)}
        for u in self.nodes:
            for v in self.edges.get(u, []):
                self.nodes[v] += 1
        for u in self.nodes:
            if self.nodes[u] == 0:
                self.zero_indegree.append(u)

    def topological_sort(self):
        queue = self.zero_indegree
        sorted_nodes = queue[:]
        while queue:
            logging.debug(f"queue={queue}")
            u = queue.pop(0)
            for v in self.edges.get(u, []):
                self.nodes[v] -= 1
                if self.nodes[v] == 0:
                    queue.append(v)
                    sorted_nodes.append(v)
        return sorted_nodes


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = Graph(numCourses, prerequisites)
        logging.debug(f"graph.nodes={graph.nodes}")
        logging.debug(f"graph.edges={graph.edges}")
        logging.debug(f"graph.zero_indegree={graph.zero_indegree}")
        sorted_nodes = graph.topological_sort()
        return [] if len(sorted_nodes) != numCourses else sorted_nodes


print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(1, []))
print(Solution().findOrder(2, [[0, 1]]))
