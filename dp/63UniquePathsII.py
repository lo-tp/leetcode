class Solution(object):
    def uniquePathsWithObstacles(self, g):
        v_sz, h_sz = len(g), len(g[0])
        dp = [[0 for _ in xrange(0, h_sz)] for _ in xrange(0, v_sz)]
        if not g[0][0]:
            dp[0][0] = 1
            for v in xrange(0, v_sz):
                for h in xrange(0, h_sz):
                    if dp[v][h] and not g[v][h]:
                        if h+1 < h_sz:
                            dp[v][h+1] += dp[v][h]
                        if v+1 < v_sz:
                            dp[v+1][h] += dp[v][h]
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, g):
        v_sz, h_sz = len(g), len(g[0])
        dp = [[0 for _ in xrange(0, h_sz)] for _ in xrange(0, v_sz)]
        if not g[0][0]:
            dp[0][0] = 1
            for v in xrange(0, v_sz):
                for h in xrange(0, h_sz):
                    if dp[v][h] and not g[v][h]:
                        if h+1 < h_sz:
                            dp[v][h+1] += dp[v][h]
                        if v+1 < v_sz:
                            dp[v+1][h] += dp[v][h]
        return 0 if g[-1][-1] else dp[-1][-1]

    def uniquePathsWithObstacles(self, g):
        if g[0][0] or g[-1][-1]:
            return 0
        v_sz, h_sz = len(g), len(g[0])
        t, dp = 1, []
        for i in g[0]:
            if i:
                t = 0
            dp.append(t)

        for v in xrange(1, v_sz):
            tmp = dp[:]
            if g[v][0]:
                tmp[0] = 0
            for h in xrange(1, h_sz):
                tmp[h] += -tmp[h] if g[v][h] else tmp[h-1]
            dp = tmp
        return dp[-1]
