class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.psum = matrix

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if j > 0:
                    self.psum[i][j] += self.psum[i][j-1] 
                if i > 0:
                    self.psum[i][j] += self.psum[i-1][j]
                if i > 0 and j > 0:
                    self.psum[i][j] -=  self.psum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.psum[row2][col2]
        if row1 > 0:
            ans -= self.psum[row1-1][col2]

        if col1 > 0:
            ans -= self.psum[row2][col1-1]

        if row1 > 0 and col1 > 0:
            ans += self.psum[row1-1][col1-1]

        return ans




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)