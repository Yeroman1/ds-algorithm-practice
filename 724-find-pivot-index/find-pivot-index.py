class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        p = [0] * n
        p[0] = nums[0]
        for i in range(1, n):
            p[i] = p[i - 1] + nums[i]
        
        for i in range(n):
            ls = p[i - 1] if i > 0 else 0
            rs = p[n - 1] - p[i]
            
            if ls == rs:
                return i
        
        return -1