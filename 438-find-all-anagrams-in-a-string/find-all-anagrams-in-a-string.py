class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sp=sorted(p)
        r=[]
        for i in range(len(s)-len(p)+1):
            if sorted(s[i:i+len(p)])==sp:
                r.append(i)
        return r



