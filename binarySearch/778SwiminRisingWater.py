class Solution(object):
    def swimInWater(self, grid):
        sz = len(grid)
        l, r, res = max(grid[0][0], grid[-1][-1]), sz*sz-1, sz*sz-1
        while l <= r:
            flag, seen, stack, m = False, set(), [(0, 0)], l+(r-l)/2
            while stack:
                i, j = stack.pop()
                if i == sz-1 and j == sz-1:
                    flag = True
                    break
                if grid[i][j] in seen:
                    continue
                seen.add(grid[i][j])
                for t, te in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if t >= 0 and t < sz and te >= 0 and te < sz and grid[t][te] <= m:
                        stack.append((t, te))
            if flag:
                res = m
                r = m-1
            else:
                l = m+1
        return res

