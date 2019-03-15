class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        prev1, prev2 = 1, 2
        for i in xrange(2, n):
            prev1, prev2 = prev2, prev1+prev2
        return prev2
