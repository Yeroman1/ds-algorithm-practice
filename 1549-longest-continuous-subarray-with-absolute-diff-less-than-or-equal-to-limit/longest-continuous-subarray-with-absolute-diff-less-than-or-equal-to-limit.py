from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        increasing = deque()
        decreasing = deque()
        n = len(nums)
        j = 0
        ans = 1
        for i in range(n):
            while increasing and nums[i] > increasing[-1]:
                increasing.pop()
            increasing.append(nums[i])
            while decreasing and nums[i] < decreasing[-1]:
                decreasing.pop()
            decreasing.append(nums[i])
            if increasing[0] - decreasing[0] > limit:
                if nums[j] == increasing[0]:
                    increasing.popleft()
                if nums[j] == decreasing[0]:
                    decreasing.popleft()
                j += 1
            ans = max(ans, i - j + 1)
        return ans