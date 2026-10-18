import heapq

EDGES = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "D", 8),
    ("C", "E", 10), ("D", "E", 2), ("D", "F", 6), ("E", "F", 3),
]


def build_graph(edges):
    graph = {}
    for a, b, weight in edges:
        graph.setdefault(a, []).append((b, weight))
        graph.setdefault(b, []).append((a, weight))
    return graph


def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    prev = {}
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        d, node = heapq.heappop(queue)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            nd = d + weight
            if nd < dist[neighbor]:
                dist[neighbor] = nd
                prev[neighbor] = node
                heapq.heappush(queue, (nd, neighbor))
    return dist, prev


def path_to(prev, start, target):
    path = [target]
    while path[-1] != start:
        path.append(prev[path[-1]])
    return list(reversed(path))


def main():
    graph = build_graph(EDGES)
    dist, prev = dijkstra(graph, "A")
    for node in sorted(dist):
        print(f"{node}: {dist[node]}")
    print("Path:", " -> ".join(path_to(prev, "A", "F")))


if __name__ == "__main__":
    main()
