class Solution(object):
    def maxWidthRamp(self, A):
        res, size = 0, len(A)
        for i in xrange(0, size):
            end = size-1
            while end != i and A[end] < A[i]:
                end -= 1
            res = max(res, end-i)
        return res


