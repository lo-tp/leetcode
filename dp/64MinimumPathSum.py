class Solution(object):
    def minPathSum(self, grid):
        verticalSize=len(grid)
        horizontalSize=len(grid[0])
        verticalIndex=0
        while verticalIndex<verticalSize:
            horizontalIndex=0
            while horizontalIndex<horizontalSize:
                if verticalIndex==0 and horizontalIndex==0:
                    horizontalIndex+=1
                    continue;
                if verticalIndex==0:
                        grid[verticalIndex][horizontalIndex]+=grid[verticalIndex][horizontalIndex-1]
                elif horizontalIndex==0:
                        grid[verticalIndex][horizontalIndex]+=grid[verticalIndex-1][horizontalIndex]
                else:
                    grid[verticalIndex][horizontalIndex]+=min(grid[verticalIndex-1][horizontalIndex], grid[verticalIndex][horizontalIndex-1])
                horizontalIndex+=1
            verticalIndex+=1
        return grid[verticalSize-1][horizontalIndex-1];

    def minPathSum(self, grid):
        v, h = len(grid), len(grid[0])
        dp, tmp = [grid[0][0]]*h, [0]*h
        for i in range(1, h):
            dp[i] = dp[i-1]+grid[0][i]

        for i in range(1, v):
            tmp[0] = grid[i][0]+dp[0]
            for j in range(1, h):
                tmp[j] = min(dp[j], tmp[j-1])+grid[i][j]
            tmp, dp = dp, tmp
        return dp[-1]
