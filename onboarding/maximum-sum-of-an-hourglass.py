class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in range(len(grid)-2):
            for col in range(1,len(grid[0])-1):
                total = grid[row][col]
                total += grid[row][col-1] + grid[row][col+1]
                total += grid[row+1][col] + sum(grid[row+2][col-1:col+2])
                ans = max(total, ans)
        return ans
