class Solution(object):
    def minDeletionSize(self, A):
        inner_sz, res = len(A[0]), set()
        for i in range(0, len(A)-1):
            for index in range(0, inner_sz):
                if index not in res:
                    if A[i][index] > A[i+1][index]:
                        res.add(index)
                    elif A[i][index] < A[i+1][index]:
                        break
        return len(res)
