class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        t=word

        while t in sequence:
            c+=1
            t+=word
        return c