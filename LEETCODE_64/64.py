class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        nRows,nCols = len(grid),len(grid[0])
        for i in range(1,nCols):
            grid[0][i]+=grid[0][i-1]
        for r in range(1,nRows):
            for c in range(nCols):
                grid[r][c] += min(
                    grid[r][c-1] if c-1>=0 else float("inf"),
                    grid[r-1][c]
                )
        return grid[-1][-1]
