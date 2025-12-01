class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid:list[list[int]]) -> int:

        nRows,nCols = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0
        obstacleGrid[0][0] = 1
        for i in range(nRows):
            for j in range(nCols):
                if i == 0 and j == 0: continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                obstacleGrid[i][j] = (obstacleGrid[i-1][j] if i-1>=0 else 0) + (obstacleGrid[i][j-1] if j-1>=0 else 0)
        return obstacleGrid[-1][-1]
        
if __name__ == "__main__":
    TEST_CASES = (
        ([[0,0,0],[0,1,0],[0,0,0]],2),
    )
    sol = Solution()
    for i,(arr,expected) in enumerate(TEST_CASES):
        res = sol.uniquePathsWithObstacles(arr)
        assert res == expected, f"Expected {expected}, but found {res}"
        print(f"Test Case {i}: Passed")