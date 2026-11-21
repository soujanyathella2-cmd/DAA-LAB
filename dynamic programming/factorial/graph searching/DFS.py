graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    node = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices separated by space: ").split()
    graph[node] = neighbors

start = input("Enter starting vertex: ")

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)