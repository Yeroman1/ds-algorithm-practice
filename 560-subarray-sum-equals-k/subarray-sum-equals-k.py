class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        s = 0
        m = {0: 1}

        for x in nums:
            s += x
            
            if s - k in m:
                c += m[s - k]
            
            m[s] = m.get(s, 0) + 1
        
        return c