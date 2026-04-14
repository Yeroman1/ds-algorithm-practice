class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        a = [[0]*n for _ in range(m)]
        l = 0
        if len(original)==n*m:
            for i in range(m):
                for j in range(n):
                    a[i][j] = original[l]
                    l += 1
            return  a
        else:
            return  []
          