class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = 0
        nsv = 1
        
        for num in nums:
            ps += num
            nsv = max(nsv, 1 - ps)
        
        return nsv