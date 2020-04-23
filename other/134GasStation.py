class Solution(object):
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
