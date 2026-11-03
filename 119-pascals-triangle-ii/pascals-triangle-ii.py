class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        def pascal(n):
            if n == 0:
                return [1]

            p = pascal(n-1)
            p_next = [1] * (n+1)

            for i in range(len(p_next)):
                if i != 0 and i != n:
                    p_next[i] = p[i] + p[i-1]

            return p_next
        
        return pascal(rowIndex)