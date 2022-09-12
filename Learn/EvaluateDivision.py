from typing import *


class Graph:
    def __init__(self, edges, values):
        self.nodes = set()
        self.edges = {}
        for edge, value in zip(edges, values):
            self.edges.setdefault(edge[0], []).append((edge[1], value))
            self.edges.setdefault(edge[1], []).append((edge[0], 1/value))
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])

    def dfs(self, source, target):
        seen = set((source,))
        result = 1

        def helper(u):
            nonlocal result
            if u == target:
                return 1
            for v, w in self.edges.get(u, []):
                if v in seen:
                    continue
                seen.add(v)
                result = w * helper(v)
                if result >= 0:
                    return result
                seen.remove(v)
            return -1
        output = helper(source)
        if source not in self.nodes:
            return -1
        # print(f"({source},{target})={output}")
        return output


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Graph(equations, values)
        # print(graph.edges)

        def calc():
            for query in queries:
                u, v = query
                result = graph.dfs(u, v)
                yield result
        output = list(calc())
        print(output)
        return output


if __name__ == "__main__":
    Solution().calcEquation([["a", "b"], ["b", "c"]],
                            [2.0, 3.0],
                            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    Solution().calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]],
                            [1.5, 2.5, 5.0],
                            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
    Solution().calcEquation([["a", "b"]],
                            [0.5],
                            [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]])
    Solution().calcEquation([["a", "aa"]],
                            [9.0],
                            [["aa", "a"], ["aa", "aa"]])
    Solution().calcEquation([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
                            [3.0, 4.0, 5.0, 6.0],
                            [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]])
