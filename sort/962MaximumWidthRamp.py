class Solution(object):
    def maxWidthRamp(self, A):
        indexes = sorted(
            [index for index in xrange(0, len(A))], key=lambda i: A[i])
        res, minimum = 0, maxint
        for i in indexes:
            res = max(res, i-minimum)
            minimum = min(i, minimum)
        return res


    def maxWidthRampTLE(self, A):
        res, size = 0, len(A)
        for i in xrange(0, size):
            end = size-1
            while end != i and A[end] < A[i]:
                end -= 1
            res = max(res, end-i)
        return res


