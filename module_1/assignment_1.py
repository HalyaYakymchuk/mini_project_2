"""First code task"""

def get_scc_sizes(filename):
    """outputs the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes"""
    edges = []
    max_node = 0

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue

            u, v = int(parts[0]), int(parts[1])
            if u == v:
                continue
            edges.append((u, v))
            if u > max_node:
                max_node = u
            if v > max_node:
                max_node = v

    n = max_node
    adj = [[] for _ in range(n + 1)]
    adj_rev = [[] for _ in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)
        adj_rev[v].append(u)

    del edges

    order = []
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                u, idx = stack[-1]
                visited[u] = True

                if idx < len(adj_rev[u]):
                    v = adj_rev[u][idx]
                    stack[-1] = (u, idx + 1)
                    if not visited[v]:
                        stack.append((v, 0))
                else:
                    order.append(stack.pop()[0])

    visited = [False] * (n + 1)
    scc_size = []

    for i in reversed(order):
        if not visited[i]:
            size = 0
            stack = [i]
            visited[i] = True

            while stack:
                u = stack.pop()
                size += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            scc_size.append(size)


    scc_size.sort(reverse=True)
    result = scc_size[:5]
    while len(result) < 5:
        result.append(0)

    return ",".join(map(str, result))

print(get_scc_sizes("SCC.txt"))
