edges = [
    (2, 'A', 'B'),
    (6, 'A', 'C'),
    (3, 'A', 'D'),
    (5, 'B', 'D'),
    (4, 'C', 'D')
]

edges.sort()

parent = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D'
}

def find(node):
    while parent[node] != node:
        node = parent[node]
    return node

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a
        return True

    return False

total_cost = 0
count = 0

print("Edges in Minimum Spanning Tree:")

for weight, u, v in edges:
    if union(u, v):
        print(u, "-", v, "=", weight)
        total_cost += weight
        count += 1

        if count == len(parent) - 1:
            break

print("Minimum cost =", total_cost)