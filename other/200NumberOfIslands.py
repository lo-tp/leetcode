class Solution(object):
    def numIslands(self, grid):
        res, columnSz = 0, len(grid)
        if columnSz:
            rowSz = len(grid[0])
            if rowSz:
                stack, dp = [], [[0]*rowSz for _ in xrange(columnSz)]
                for c in xrange(0, columnSz):
                    for r in xrange(0, rowSz):
                        if grid[c][r] == '1' and not dp[c][r]:
                            res += 1
                            stack.append((c, r))
                            while stack:
                                c1, r1 = stack.pop()
                                if c1 >= 0 and r1 >= 0 and c1 < columnSz and r1 < rowSz and not dp[c1][r1] and grid[c1][r1] == '1':
                                    dp[c1][r1] = 1
                                    stack.append((c1-1, r1))
                                    stack.append((c1+1, r1))
                                    stack.append((c1, r1-1))
                                    stack.append((c1, r1+1))
        return res
