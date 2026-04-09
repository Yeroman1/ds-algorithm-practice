class Solution:
    def pivotInteger(self, n: int) -> int:
        s=sum(list(range(1, n+1)))
        cs=0

        for i in range(1, n+1):
            cs+=i
            if cs==s-cs+i:
                return i
        return -1
