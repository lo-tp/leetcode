class Solution(object):
    def isSelfCrossing(self, x):
        sz = len(x)
        if sz >= 4 and x[0] >= x[2] and x[1] <= x[3]:
            return True
        if sz >= 5:
            if x[1] >= x[3] and x[2] <= x[4]:
                return True
            elif x[1] == x[3] and (x[0]+x[4]) >= x[2]:
                return True
        if sz > 5:
            for i in xrange(sz-1, 4, -1):
                if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                    return True
                elif (x[i]+x[i-4] >= x[i-2]) and x[i-1] == x[i-3]:
                    return True
                elif x[i-2] > x[i-4] and x[i-2] <= (x[i]+x[i-4]) and x[i-3] > x[i-1] and x[i-3] > x[i-5] and (x[i-1]+x[i-5]) >= x[i-3]:
                    return True
        return False
