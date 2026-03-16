class Solution:
    def searchInsert(self, nums, target):
        s = 0
        e = len(nums) - 1
    
        while s <= e:
            m = (e + s) // 2

            if nums[m] == target:
                return m

            if nums[m] < target:
                s = m + 1
            else:
                e = m - 1

        return s