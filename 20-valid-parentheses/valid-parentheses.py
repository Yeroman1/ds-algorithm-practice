class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if stack and d[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
                
