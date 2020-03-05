class Solution(object):    
    def isIdealPermutationButTLE(self, A):
        sz = len(A)
        for i in xrange(0, sz-2):
            for j in xrange(i+2, sz):
                if A[i] > A[j]:
                    return False
        return True

    def isIdealPermutation(self, A):
        minimum, sz = A[-1], len(A)
        for i in xrange(sz-3, -1, -1):
            if A[i] > minimum:
                return False
            minimum = min(minimum, A[i+1])
        return True
