
                                    # Approach: Kadane's Algorithm


n = int(input())
nums = list(map(int, input().split()))
current_sum = nums[0]
max_sum = nums[0]
for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])           # Time Complexity: O(n)
    max_sum = max(max_sum, current_sum)                         # Space Complexity: O(1)
print(max_sum)



