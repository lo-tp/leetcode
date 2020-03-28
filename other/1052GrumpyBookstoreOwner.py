class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        sz, t = len(customers), 0
        for i in xrange(0, sz):
            if not grumpy[i]:
                t += customers[i]
        for i in xrange(0, X):
            if grumpy[i]:
                t += customers[i]
        te, res = 0, t
        for i in xrange(X, sz):
            if grumpy[te]:
                t -= customers[te]
            if grumpy[i]:
                t += customers[i]
            res = max(res, t)
            te += 1
        return res
