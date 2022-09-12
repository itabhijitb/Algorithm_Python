from typing import *
import logging
logging.basicConfig(level=logging.WARN)


class Graph:
    def __init__(self, nodes, edges):
        self.edges = {}
        self.zero_indegree = []
        for edge in edges:
            u, v = edge
            if u == v:
                continue
            self.edges.setdefault(v, set()).add(u)
        self.nodes = {u: 0 for u in nodes}
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
            u = queue.pop(0)
            for v in self.edges.get(u, []):
                self.nodes[v] -= 1
                if self.nodes[v] == 0:
                    queue.append(v)
                    sorted_nodes.append(v)
        return sorted_nodes


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        edges = []
        nodes = set(ch for word in words for ch in word)
        for curr_word, next_word in zip(words, words[1:]):
            it_curr_word, it_next_word = iter(curr_word), iter(next_word)
            for u, v in zip(curr_word, next_word):
                if u != v:
                    edges.append((v, u))  # u ---> v
                    break

        graph = Graph(nodes, edges)
        logging.debug(graph.edges)
        sorted_nodes = graph.topological_sort()
        logging.debug(sorted_nodes)
        return ''.join(sorted_nodes)


print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(Solution().alienOrder(["z", "x"]))
print(Solution().alienOrder(["z"]))
print(Solution().alienOrder(["z", "x", "z"]))
print(Solution().alienOrder(["z", "z"]))
print(Solution().alienOrder(["ab", "adc"]))
print(Solution().alienOrder(["ac", "ab", "zc", "zb"]))
