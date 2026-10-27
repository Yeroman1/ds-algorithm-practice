class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")", "[":"]", "{":"}"}
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if d[top]!=i:
                    return False
                
        return not stack