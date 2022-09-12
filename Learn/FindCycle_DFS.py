from collections import defaultdict
from typing import List
import doctest


class DFS:
    def __init__(self, edges):
        self.adj = defaultdict(list)
        for (u, v) in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

    def __call__(self):
        seen = set()

        def helper(node, parent):
            nonlocal cycle_found
            if cycle_found:
                return cycle_found
            for v in self.adj[node]:
                if v == parent:
                    continue
                if v in seen:
                    cycle_found = True
                    return
                seen.add(v)
                helper(v, node)
                seen.remove(v)
            return cycle_found
        cycle_found = False
        helper(0, set())
        return cycle_found


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        return DFS(edges)()


print(Solution().valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(Solution().valid_tree(2, [[0, 1]]))
