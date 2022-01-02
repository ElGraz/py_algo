

class Dijkstra:
    def __init__(self, nodes: list, edges: dict[tuple, int]):
        self.nodes = nodes
        self.edges = edges

    def solve(self, source_idx: int = 0):
        costs = {v: float('inf') for v in self.nodes}
        costs[0] = 0

        adj_nodes = {v: {} for v in self.nodes}
        for (start, end), cost in self.edges.items():
            adj_nodes[start][end] = cost
            adj_nodes[end][start] = cost

        print(f"Adj_nodes: {adj_nodes} ")

        tmp_nodes = list(self.nodes)

        while len(tmp_nodes) > 0:
            upper_bounds = {v: costs[v] for v in tmp_nodes}
            u = min(upper_bounds, key=upper_bounds.get)
            print(f'u {u}')
            tmp_nodes.remove(u)
            print(f"Upper_bounds {upper_bounds}")

            for v, cost_uv in adj_nodes[u].items():
                cost = costs[u]+cost_uv
                if cost < costs[v]:
                    costs[v] = cost
                    print(f"cost from 0 to {v} is now {costs[v]} (through {u})")
        return costs


if __name__ == "__main__":
    nodes = [0, 1, 2, 3]
    edges = {(0, 1): 5, (0, 2): 3, (1, 3): 5, (2, 3): 1}

    dij = Dijkstra(nodes, edges)
    res = dij.solve()

    print(res)
