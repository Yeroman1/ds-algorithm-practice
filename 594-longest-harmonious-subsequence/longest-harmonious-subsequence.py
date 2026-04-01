class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        r = 0
        
        for n in c:
            if n + 1 in c:
                r = max(r, c[n] + c[n + 1])
        
        return r