class Solution(object):
    def equalSubstring(self, x, t, maxCost):
        s, res, cost = 0, 0, 0
        for e in xrange(0, len(x)):
            cost += abs(ord(x[e])-ord(t[e]))
            while cost > maxCost:
                cost -= abs(ord(x[s])-ord(t[s]))
                s += 1
            res = max(res, e-s+1)
        return res
