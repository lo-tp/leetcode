from collections import defaultdict


class Solution(object):
    def longestArithSeqLength(self, A):
        res = 0
        if A:
            res, size, dp = 1, len(A), [defaultdict(lambda: 1) for i in A]
            for index in xrange(size-1, -1, -1):
                num = A[index]
                for i, next_num in enumerate(A[index+1: size]):
                    next_index = index+i+1
                    offset = next_num-num
                    dp[index][offset] = max(
                        dp[next_index][offset]+1, dp[index][offset])
                    res = max(res, dp[index][offset])
        return res

