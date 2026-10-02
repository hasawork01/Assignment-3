


                    # Problem 3: Maximum Subarray Sum

n = int(input())
nums = list(map(int, input().split()))
max_sum = nums[0]
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += nums[j]                      # Time Complexity: O(n^2)
        max_sum = max(max_sum, current_sum)         # Space Complexity: O(1)
print(max_sum)




