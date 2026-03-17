class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        l=list(s.split())
        return len(l[-1])
        