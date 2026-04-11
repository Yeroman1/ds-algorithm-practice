class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        b={')':'(',']':'[','}':'{'}
        for c in s:
            if c in b:
                d=a.pop() if a else '#'
                if b[c]!=d:
                    return False
            else:
                a.append(c)
        return not a