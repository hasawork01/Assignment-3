                            
                            
                            # Problem 1: Two Sum
                            # Approach: Brute Force


n = int(input())
nums = list(map(int, input().split()))
target = int(input())
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:     # Time Complexity: O(n^2)
            print(i, j)                     # Space Complexity: O(1)
            break