class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        row = len(mat)
        r = row-1
        for l in range(row):
            if l != r-l:
                ans += mat[l][l] + mat[l][r-l]
        
            else:
                ans += mat[l][l]
        return ans


