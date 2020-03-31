from sys import maxint



class Solution(object):
    def numMovesStonesII(self, s):
        sz, l, r = len(s), 0, 0
        s.sort()
        minimum, maximum = sz, max(s[-1]-s[1]-sz+2, s[-2]-s[0]-sz+2)
        for r in xrange(0, sz):
            while s[r]-s[l]+1 > sz:
                l += 1
            if r-l+1 == sz-1 and s[r] == s[l]+sz-2:
                minimum = min(2, minimum)
            else:
                minimum = min(minimum, sz-r+l-1)
        return [minimum, maximum]
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

