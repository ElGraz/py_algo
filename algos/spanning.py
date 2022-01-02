def spanning(nodes, edges):
    adj_list = {node: set() for node in nodes}

    for path in edges.keys():
        adj_list[path[0]].add(path[1])
        adj_list[path[1]].add(path[0])
    print(adj_list)

    span_path = []

    tmp_nodes = set(nodes)
    curr_node = nodes[0]
    span_path.append(curr_node)
    tmp_nodes.remove(curr_node)

    while len(tmp_nodes) > 0:
        ok = False
        print(f'curr node {curr_node}')
        for next_node in adj_list[curr_node]:
            if next_node in tmp_nodes:
                curr_node = next_node
                span_path.append(next_node)
                tmp_nodes.remove(next_node)
                ok = True
                break
        if not ok:
            break

    return span_path 


if __name__ == "__main__":
    nodes = [0, 1, 2, 3]
    edges = {(0, 1): 1, (0, 2): 3, (1, 3): 5, (2, 3): 1}
    span = spanning(nodes, edges)
    print(span)
