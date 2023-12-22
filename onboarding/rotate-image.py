class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        store = set()
        for i in range(n):
            for j in range(n):
                if (j,i) not in store:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    store.add((i,j))
        for row in matrix:
            row.reverse()