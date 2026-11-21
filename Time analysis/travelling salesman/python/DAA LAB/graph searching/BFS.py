graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    node = input("Enter vertex: ")
    neighbors = input("Enter adjacent vertices separated by space: ").split()
    graph[node] = neighbors

start = input("Enter starting vertex: ")

def bfs(graph, start):
    visited = {start}
    queue = [start]
    index = 0

    while index < len(queue):
        node = queue[index]
        index += 1

        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS Traversal:")
bfs(graph, start)