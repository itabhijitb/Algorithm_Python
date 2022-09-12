from typing import *
from heapq import heappush


class Graph:
    def __init__(self, edges):
        self.edges = dict()
        self.nodes = set()
        self.edge_count = 0
        for edge in edges:
            u, v = edge
            self.edge_count += 1
            self.nodes.add(u)
            self.nodes.add(v)
            self.edges.setdefault(u, []).append(v)
        for u, v in self.edges.items():
            v.sort()

    def dfs(self, source):
        seen = set()
        route = []
        found = False

        def recurse(u, path):
            nonlocal found
            nonlocal route
            if found:
                return
            if len(path) == self.edge_count + 1:
                route = path[:]
                found = True
                return
            for ix, v in enumerate(self.edges.get(u, [])):
                if (u, ix) not in seen:
                    seen.add((u, ix))
                    recurse(v, path + (v, ))
                    seen.remove((u, ix))
        recurse(source, (source, ))
        return route


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = Graph(tickets)
        return graph.dfs("JFK")


tickets = [["EZE", "TIA"], ["EZE", "AXA"], ["AUA", "EZE"], ["EZE", "JFK"], ["JFK", "ANU"], ["JFK", "ANU"], [
    "AXA", "TIA"], ["JFK", "AUA"], ["TIA", "JFK"], ["ANU", "EZE"], ["ANU", "EZE"], ["TIA", "AUA"]]
print(Solution().findItinerary(tickets))
