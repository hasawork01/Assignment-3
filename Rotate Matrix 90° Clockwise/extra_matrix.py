

                    # Problem 2: Rotate Matrix 90 Degrees Clockwise

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
rotated = [[0] * n for _ in range(n)]
for i in range(n):                                     # Time Complexity: O(n^2) 
    for j in range(n):                                 # Space Complexity: O(n^2)
        rotated[j][n - 1 - i] = matrix[i][j]
for row in rotated:
    print(*row)