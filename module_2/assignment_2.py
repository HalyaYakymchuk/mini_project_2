"""Dijkstra algorithm"""

def load_graph(filename):
    """parsing data from the given file"""
    graph = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            if not parts:
                continue

            node = int(parts[0])
            edges = []
            for item in parts[1:]:
                neighbour, weight = map(int, item.split(","))
                edges.append((neighbour, weight))
            graph[node] = edges
    return graph


def dijkstra_algo(graph, start_node):
    """algorithm implementation"""
    distances = {node: 1000000 for node in graph}
    distances[start_node] = 0
    visited = set()
    num_nodes = len(graph)

    for _ in range(num_nodes):
        current_node = None
        min_dist = 1000001

        for node in graph:
            if node not in visited and distances[node] < min_dist:
                min_dist = distances[node]
                current_node = node

        if current_node is None:
            break
        visited.add(current_node)

        for neighbour, weight in graph.get(current_node, []):
            if neighbour not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance

    return distances


graph = load_graph('test2.txt')
results = dijkstra_algo(graph, 1)

target_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
answer = ",".join(str(results[node]) for node in target_nodes)
print(answer)
