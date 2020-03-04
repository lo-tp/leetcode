class Solution(object):    
    def isIdealPermutation(self, A):
        sz = len(A)
        for i in xrange(0, sz-2):
            for j in xrange(i+2, sz):
                if A[i] > A[j]:
                    return False
        return True

