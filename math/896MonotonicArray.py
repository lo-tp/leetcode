class Solution(object):
    def isMonotonic(self, A):
        t, sz = 1, len(A)
        while t < sz and A[t-1] == A[t]:
            t += 1
        if t < sz:
            flag = A[t-1] < A[t]
            for i in xrange(t, sz):
                if A[i-1] != A[i] and flag ^ (A[i-1] < A[i]):
                    return False
        return True
