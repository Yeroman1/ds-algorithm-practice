class Solution:
    def minMoves(self, nums: List[int]) -> int:
        guddaa=max(nums)
        d_xiqqaa=0
        for i in nums:
            d_xiqqaa+=(guddaa-i)
        
        return d_xiqqaa