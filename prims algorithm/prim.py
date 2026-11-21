graph = [
    [0, 2, 6, 3],
    [2, 0, 0, 5],
    [6, 0, 0, 4],
    [3, 5, 4, 0]
]

n = len(graph)
visited = [False] * n
visited[0] = True
total_cost = 0

print("Edges in Minimum Spanning Tree:")

for _ in range(n - 1):
    minimum = float('inf')
    x = -1
    y = -1

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(chr(65 + x), "-", chr(65 + y), "=", minimum)

    total_cost += minimum
    visited[y] = True

print("Minimum cost =", total_cost)