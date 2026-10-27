class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")", "[":"]", "{":"}"}
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if stack:
                    if d[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
