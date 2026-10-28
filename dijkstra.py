import heapq


def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    pred = [None] * n

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if d != dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                pred[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, pred


n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

m = int(input("Enter number of edges: "))

for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())

    graph[u].append((v, w))
    graph[v].append((u, w))


source = int(input("Enter source vertex: "))

dist, pred = dijkstra(graph, source)

print("Shortest distances from source", source)

for i in range(n):
    if dist[i] == float('inf'):
        print(i, ": Unreachable")
    else:
        print(i, ":", dist[i])
