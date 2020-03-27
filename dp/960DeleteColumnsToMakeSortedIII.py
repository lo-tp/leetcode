class Solution(object):
    def minDeletionSize(self, A):
        v_sz, h_sz, dp = len(A), len(A[0]), [1 for _ in A[0]]
        for h in xrange(1, h_sz):
            for j in xrange(0, h):
                flag = True
                for v in xrange(0, v_sz):
                    if ord(A[v][h]) < ord(A[v][j]):
                        flag = False
                        break
                if flag:
                    dp[h] = max(dp[h], dp[j]+1)
        return h_sz - max(dp)

