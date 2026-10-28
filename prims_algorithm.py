import heapq


def prim(graph, n):
    visited = [False] * n
    pq = [(0, 0, -1)]
    mst = []
    total_weight = 0

    while pq and len(mst) < n - 1:
        weight, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, weight))
            total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v, u))

    if len(mst) != n - 1:
        print("Graph is disconnected.")
        return

    print("Edges in Minimum Spanning Tree:")

    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Total weight of MST:", total_weight)


n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

m = int(input("Enter number of edges: "))

for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())

    graph[u].append((v, w))
    graph[v].append((u, w))


prim(graph, n)
