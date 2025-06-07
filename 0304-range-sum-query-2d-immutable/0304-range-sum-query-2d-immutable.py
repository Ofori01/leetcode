class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        # with padding
        killers = [[0]*(m +1) for _ in range(n+1)]
        

        for i in range(n):
            for j in range(m):
                killers[i+1][j+1]=  matrix[i][j] + killers[i+1][j] + killers[i][j+1] - killers[i][j]
        self.killers = killers


        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        killers = self.killers
        return killers[row2+1][col2+1] -  killers[row1][col2+1] - killers[row2+1][col1] + killers[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)