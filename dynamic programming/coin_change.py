
def matrix_chain_order(p, n):
    # dp[i][j] stores minimum number of scalar multiplications
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # L is the chain length
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]


# Take input from user
num = int(input("Enter the number of matrices: "))

print("Enter the dimensions:")
print("For matrices A1, A2, ..., An, enter n+1 dimensions.")

p = []

for i in range(num + 1):
    value = int(input(f"Enter dimension {i + 1}: "))
    p.append(value)

# Calculate minimum multiplication cost
minimum_cost = matrix_chain_order(p, num + 1)

print("\nMinimum number of scalar multiplications:", minimum_cost)