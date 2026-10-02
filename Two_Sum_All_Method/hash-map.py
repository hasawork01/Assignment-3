                                
                                # Problem 1 Two Sum  Approach: Hash Map 
                                

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
seen = {}
for i in range(n):
    complement = target - nums[i]       # Time Complexity: O(n)
    if complement in seen:              # Space Complexity: O(n)
        print(seen[complement], i)
        break
    seen[nums[i]] = i

