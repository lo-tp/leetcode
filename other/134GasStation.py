class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        sz = len(gas)
        t, l, r = gas[sz-1]-cost[sz-1], sz-1, 0
        while l > r:
            if t >= 0:
                t += gas[r]-cost[r]
                r += 1
            else:
                l -= 1
                t += gas[l]-cost[l]
        return l if t >= 0 else -1

    def canCompleteCircuit(self, gas, cost):
        sz = len(gas)
        for i in xrange(0, sz):
            te, t = 0, 0
            while te != sz:
                tmp = (i+te) % sz
                t += gas[tmp]
                t -= cost[tmp]
                if t < 0:
                    break
                te += 1
            if te == sz:
                return i
        return -1
