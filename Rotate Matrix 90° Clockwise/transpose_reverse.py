
                            # Approach: Transpose + Reverse


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):                                          # Time Complexity: O(n^2)
    for j in range(i + 1, n):                                               
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]     # Space Complexity: O(1)
for i in range(n):
    matrix[i].reverse()
for row in matrix:
    print(*row)