


                                # Approach: Layer-by-Layer / 4-Way Rotation
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
top = 0
bottom = n - 1
left = 0
right = n - 1
while top < bottom:
    for i in range(right - left):
        temp = matrix[top][left + i]
        matrix[top][left + i] = matrix[bottom - i][left]
        matrix[bottom - i][left] = matrix[bottom][right - i]            # Time Complexity: O(n^2)
        matrix[bottom][right - i] = matrix[top + i][right]              # Space Complexity: O(1)
        matrix[top + i][right] = temp
    top += 1
    bottom -= 1
    left += 1
    right -= 1
for row in matrix:
    print(*row)

        

        

        
