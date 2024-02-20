class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = []
        total = 0
        for row in grid:
            rowMax.append(max(row))

        colMax = []

        for col in range(n):
            curr_max = grid[0][col]
            for row in range(n):
                curr_max = max(curr_max, grid[row][col])

            colMax.append(curr_max)

        for i in range(n):
            for j in range(n):
                num = grid[i][j]

                row = rowMax[i]
                col = colMax[j]
                total += min(row, col) - num  

        return total




                


