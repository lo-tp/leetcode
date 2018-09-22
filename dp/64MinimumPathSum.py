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

