class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,m=0,0
        a=set()
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1

            m=max(m, r-l+1)
            a.add(s[r])
            
        return m
