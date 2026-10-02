
                                # Problem 1: Two Sum
                                # Approach: Sorting + Two Pointers

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
arr = [(nums[i], i) for i in range(n)]
arr.sort()
left = 0
right = n - 1
while left < right:
    total = arr[left][0] + arr[right][0]
    if total == target:                               # Time Complexity: O(n log n)
        print(arr[left][1], arr[right][1])            # Space Complexity: O(n)
        break
    elif total < target:
        left += 1
    else:
        right -= 1

