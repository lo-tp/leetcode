from heapq import heapify, heappop, heappush


class Solution(object):
    def minFallingPathSum(self, arr):
        sz = len(arr)
        dp = [(0, i) for i in xrange(0, sz)]
        if sz > 1:
            for v in xrange(0, sz):
                tmp = []
                for h in xrange(0, sz):
                    t, te = None, None
                    if dp[0][1] == h:
                        t, te = heappop(dp)
                    tmp.append((arr[v][h]+dp[0][0], h))
                    if t != None:
                        heappush(dp, (t, te))
                dp = tmp
                heapify(dp)
            return dp[0][0]
        return arr[0][0]
