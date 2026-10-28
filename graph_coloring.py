def is_safe(graph, color, vertex, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:
            return False

    return True


def graph_coloring(graph, m, color, vertex):
    n = len(graph)

    if vertex == n:
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, vertex, c):
            color[vertex] = c

            if graph_coloring(graph, m, color, vertex + 1):
                return True

            color[vertex] = 0

    return False


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))

color = [0] * n

if graph_coloring(graph, m, color, 0):
    print("Color assignment:", color)
else:
    print("No solution exists")
