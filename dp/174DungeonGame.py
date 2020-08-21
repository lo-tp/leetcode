from sys import maxint


class Solution(object):
    def calculateMinimumHP(self, d):
        v_sz, h_sz, stack, res = len(d), len(
            d[0]), [(0, 0, 1+(d[0][0] if d[0][0] > 0 else 0), 1 - (0 if d[0][0] > 0 else d[0][0]))], maxint

        while stack:
            v, h, current, minimum = stack.pop()
            if minimum >= res:
                continue
            if v == v_sz-1 and h == h_sz-1:
                res = min(res, minimum)

            for t, te in [(t, te) for t, te in (v+1, h), (v, h+1) if t < v_sz and te < h_sz]:
                c = current+d[t][te]
                stack.append((t, te, max(c, 1), minimum-(0 if c > 0 else c-1)))
        return res

    def calculateMinimumHP(self, d):
        v_sz, h_sz, dp = len(d), len(
            d[0]), None

        for v in xrange(0, v_sz):
            tmp = []
            if not v:
                tmp.append((1+max(0, d[0][0]), 1-min(d[0][0], 0)))
            for h in xrange(0, h_sz):
                s = 1
                m = maxint
                if v:
                    t = dp[h][0]+d[v][h]
                    s = max(t, s)
                    m = dp[h][1]+(1-t if t <= 0 else 0)
                if h:
                    t = tmp[-1][0]+d[v][h]
                    s = max(t, s)
                    m = min(tmp[-1][1]+(1-t if t <= 0 else 0), m)
                if v or h:
                    tmp.append((s, m))
            dp = tmp
        return dp[-1][1]

    def calculateMinimumHP(self, d):
        v_sz, h_sz = len(d), len(
            d[0])
        dp = [1 for _ in xrange(0, h_sz)]
        dp[-1] = 1-min(0, d[-1][-1])
        for h in xrange(h_sz-2, -1, -1):
            dp[h] = max(1, dp[h+1]-d[-1][h])

        for v in xrange(v_sz-2, -1, -1):
            tmp = dp[:]
            for h in xrange(h_sz-1, -1, -1):
                tmp[h] = max(1, dp[h]-d[v][h])
                if h < h_sz-1:
                    tmp[h] = min(tmp[h], max(1, tmp[h+1]-d[v][h]))
                dp = tmp
        return dp[0]


    def calculateMinimumHP(self, d):
        v_sz, h_sz = len(d), len(
            d[0])
        dp = [maxint for _ in xrange(0, h_sz)]
        dp[-1] = 1-min(0, d[-1][-1])
        for v in xrange(v_sz-1, -1, -1):
            tmp = dp[:]
            for h in xrange(h_sz-1, -1, -1):
                if v+1 < v_sz:
                    tmp[h] = max(1, dp[h]-d[v][h])
                if h < h_sz-1:
                    tmp[h] = min(tmp[h], max(1, tmp[h+1]-d[v][h]))
                dp = tmp
        return dp[0]
