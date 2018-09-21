class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        verticalSize=len(grid)
        horizontalSize=len(grid[ 0 ])
        horizontalIndex=1
        while horizontalIndex<horizontalSize:
            grid[0][horizontalIndex]+=grid[0][horizontalIndex-1]
            horizontalIndex+=1
        verticalIndex=1
        while verticalIndex<verticalSize:
            grid[verticalIndex][0]+=grid[verticalIndex-1][0]
            verticalIndex+=1
        verticalIndex=1
        while verticalIndex<verticalSize:
            horizontalIndex=1
            while horizontalIndex<horizontalSize:
                if grid[verticalIndex-1][horizontalIndex]<grid[verticalIndex][horizontalIndex-1]:
                    grid[verticalIndex][horizontalIndex]+=grid[verticalIndex-1][horizontalIndex]
                else:
                    grid[verticalIndex][horizontalIndex]+=grid[verticalIndex][horizontalIndex-1]
                horizontalIndex+=1
            verticalIndex+=1
        return grid[verticalSize-1][horizontalSize-1]
s=Solution()
print s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
