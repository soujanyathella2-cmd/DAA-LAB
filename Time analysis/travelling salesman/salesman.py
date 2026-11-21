
from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter the cost matrix:")

cost = []
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

min_cost = float('inf')
best_path = None

# Fix starting city as 0
cities = list(range(1, n))

for path in permutations(cities):
    total_cost = cost[0][path[0]]

    for i in range(len(path) - 1):
        total_cost += cost[path[i]][path[i + 1]]

    total_cost += cost[path[-1]][0]

    if total_cost < min_cost:
        min_cost = total_cost
        best_path = (0,) + path + (0,)

print("\nMinimum travelling cost:", min_cost)
print("Best path:", " -> ".join(str(city + 1) for city in best_path))
