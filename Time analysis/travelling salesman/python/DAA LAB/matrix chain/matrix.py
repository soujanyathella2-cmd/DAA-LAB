# Matrix Chain Multiplication using Dynamic Programming

n = int(input("Enter number of matrices: "))

# Array to store dimensions
p = []

print("Enter the dimensions:")
for i in range(n + 1):
    value = int(input(f"p[{i}] = "))
    p.append(value)

# Create DP table
m = [[0 for j in range(n)] for i in range(n)]

# Chain length
for length in range(2, n + 1):

    for i in range(1, n - length + 2):

        j = i + length - 1
        m[i - 1][j - 1] = 999999

        for k in range(i, j):

            cost = (
                m[i - 1][k - 1]
                + m[k][j - 1]
                + p[i - 1] * p[k] * p[j]
            )

            if cost < m[i - 1][j - 1]:
                m[i - 1][j - 1] = cost

print("Minimum number of scalar multiplications:",
      m[0][n - 1])