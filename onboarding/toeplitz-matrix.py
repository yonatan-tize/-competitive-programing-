class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        num = len(matrix[0])
        for i in range(len(matrix)-1):
            for j in range(0, num-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False

        return True

