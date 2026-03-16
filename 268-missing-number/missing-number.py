class Solution:
    def missingNumber(self, nums):
        numbers_set = set(nums)
        n = len(nums)

        for i in range(n + 1):
            if i not in numbers_set:
                return i