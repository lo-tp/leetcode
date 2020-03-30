from sys import maxint



class Solution(object):
    def numMovesStonesII(self, stones):
        stones.sort()
        sz, low = len(stones), maxint
        seen = set(stones)
        for i in stones:
            if i+sz-1 > stones[-1]:
                break
            t = []
            for j in xrange(i, i+sz):
                if j not in seen:
                    t.append(j)
            if len(t) == 1 and t[-1] == (i+sz-1):
                low = min(low, 2)
            else:
                low = min(low, len(t))
        return [low, max(stones[-1]-stones[1]-sz+2, stones[-2]-stones[0]-sz+2)]

