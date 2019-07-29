class Solution(object):
    def numFactoredBinaryTrees(self, A):
        A.sort()
        position, mod, size = {num: i for i,
                               num in enumerate(A)}, 10 ** 9 + 7, len(A)
        dp = [1]*size
        for i, num in enumerate(A):
            for j in xrange(0, i):
                tmp = num/A[j]
                if not num % A[j] and tmp in position:
                    dp[i] += dp[j]*dp[position[tmp]]
                    dp[i] %= mod
        return sum(dp) % mod
