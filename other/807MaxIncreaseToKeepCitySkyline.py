class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        h_sz, v_sz, res = len(grid[0]), len(grid), 0
        v_max = [max(r) for r in grid]
        h_max = [grid[0][i] for i in xrange(0, h_sz)]
        for i in xrange(1, v_sz):
            for j in xrange(0, h_sz):
                h_max[j] = max(h_max[j], grid[i][j])
        for i in xrange(0, v_sz):
            for j in xrange(0, h_sz):
                res += (min(v_max[i], h_max[j])-grid[i][j])
        return res

