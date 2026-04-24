class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        pre = [[0]*(cols+1) for _ in range(rows+1)]
        
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                pre[r][c] = (
                    matrix[r-1][c-1]
                    + pre[r-1][c]
                    + pre[r][c-1]
                    - pre[r-1][c-1]
                )
        self.pre=pre
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre=self.pre
        return (
        pre[row2+1][col2+1]
        - pre[row1][col2+1]
        - pre[row2+1][col1]
        + pre[row1][col1]
    )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)