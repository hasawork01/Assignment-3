
                                    # Approach: Prefix Sum


n = int(input())
nums = list(map(int, input().split()))
prefix = 0
minimum_prefix = 0
max_sum = nums[0]
for num in nums:
    prefix += num                                           # Time Complexity: O(n)
    max_sum = max(max_sum, prefix - minimum_prefix)         # Space Complexity: O(1)
    minimum_prefix = min(minimum_prefix, prefix)
print(max_sum)




