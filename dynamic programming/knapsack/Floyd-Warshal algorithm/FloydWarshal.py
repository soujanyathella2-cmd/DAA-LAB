
INF = 99999

n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")
print("(Enter 99999 for no edge)")

dist = []

for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

# Display shortest distance matrix
print("\nShortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
