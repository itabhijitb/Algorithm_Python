from collections import defaultdict
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __iter__(self):
        yield self.u
        yield self.v


class Graph:
    def __init__(self, nodes):
        self.nodes = list(nodes)
        self.edges = defaultdict(list)

    def __iadd__(self, edge: Edge):
        if edge.v is None:
            self.nodes.append(edge.u)
        elif edge.u is None:
            self.nodes.append(edge.v)
        else:
            self.edges[edge.u].append(edge.v)
            self.nodes += [edge.u, edge.v]
        return self

    def __iter__(self):
        logging.debug(self.edges)
        for u in self.edges:
            for v in self.edges[u]:
                yield (u, v)


class UnionFind:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.heads = {u: u for u in self.graph.nodes}
        self._union()

    def find(self, u, rank=0):
        if u == self.heads[u]:
            return u, rank
        head, rank = self.find(self.heads[u], rank + 1)
        self.heads[u] = head
        return head, rank

    def _union(self):
        for edge in self.graph:
            logging.debug(f"edge={edge}")

            u, v = edge
            root_u, rank_u = self.find(u)

            root_v, rank_v = self.find(v)
            if root_u != root_v:
                if rank_u > rank_v:
                    self.heads[root_v] = root_u
                else:
                    self.heads[root_u] = root_v
            logging.debug(f"(key: {root_u}, head: {root_u})")
        logging.debug(self.heads)


g = Graph(range(10))
g += Edge(0, 1)
g += Edge(0, 2)
g += Edge(0, 3)
g += Edge(0, 4)
g += Edge(0, 5)
g += Edge(0, 6)


uf = UnionFind(g)
print(uf.find(0))
print(uf.find(1))
print(uf.find(7))
