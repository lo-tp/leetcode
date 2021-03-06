class Solution(object):
    def kInversePairsWA(self, n, k):
        if not k:
            return 1
        if k >= n:
            return 0
        dp = [[0 for _ in xrange(0, k+1)] for _ in xrange(0, n)]
        dp[0][0] = 1
        for i in xrange(1, n):
            dp[i][0] = 1
            for j in xrange(1, min(i, k)+1):
                for w in xrange(0, min(i-1, j)+1):
                    dp[i][j] += dp[i-1][w]
        return dp[n-1][k] % (10 ** 9+7)

    def kInversePairsTLE(self, n, k):
        dp = [[0 for _ in xrange(0, k+1)] for _ in xrange(0, n)]
        dp[0][0] = 1
        for i in xrange(1, n):
            dp[i][0] = 1
            for j in xrange(1, k+1):
                for m in xrange(0, min(i+1, j+1)):
                    dp[i][j] += dp[i-1][j-m]
        return dp[n-1][k]

    def kInversePairs(self, n, k):
        if not k:
            return 1
        dp = [[0 for _ in xrange(0, k+1)] for _ in xrange(0, n)]
        for i in xrange(0, k+1):
            dp[0][i] = 1
        for i in xrange(1, n):
            dp[i][0] = 1
            for m in xrange(1,  k+1):
                dp[i][m] = dp[i][m-1]
                if i >= m:
                    dp[i][m] += dp[i-1][m]
                else:
                    dp[i][m] += dp[i-1][m]-dp[i-1][m-i-1]
        return (dp[n-1][k]-dp[n-1][k-1]) % (10**9+7)

    def kInversePairs(self, n, k):
        if not k:
            return 1
        dp = [1 for _ in xrange(0, k+1)]
        for i in xrange(1, n):
            tem = [1]
            for m in xrange(1,  k+1):
                tem.append(tem[-1])
                if i >= m:
                    tem[-1] += dp[m]
                else:
                    tem[-1] += dp[m]-dp[m-i-1]
            dp = tem
        return (dp[k]-dp[k-1]) % (10**9+7)

    def kInversePairs(self, n, k):
        if not k:
            return 1
        dp = [1 for _ in xrange(0, k+1)]
        for i in xrange(1, n):
            tem = [1]
            for m in xrange(1,  k+1):
                tem.append(tem[-1])
                tem[-1] += dp[m] if i >= m else (dp[m]-dp[m-i-1])
            dp = tem

        return (dp[k]-dp[k-1]) % (10**9+7)

    def kInversePairs(self, n, k):
        dp = [[0 for _ in xrange(0, k+1)]for _ in xrange(0, n+1)]
        dp[1][0] = 1
        for i in xrange(2, n+1):
            dp[i][0] = 1
            for j in xrange(1, min(k, (n*n+n)/2)+1):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
                if j > i-1:
                    dp[i][j] -= dp[i-1][j-i]

        return dp[n][k] % (10**9+7)

    def kInversePairs(self, n, k):
        if n < 1:
            return 1
        dp = [0 for _ in xrange(0, k+1)]
        dp[0] = 1
        for i in xrange(2, n+1):
            tmp = dp[:]
            for j in xrange(1, min(k, (n*n+n)/2)+1):
                tmp[j] = tmp[j-1]+dp[j]
                if j > i-1:
                    tmp[j] -= dp[j-i]
            dp = tmp
        return dp[k] % (10**9+7)

    def kInversePairs(self, n, k):
        if not k:
            return 1
        dp = [1 for _ in xrange(0, k+1)]
        for i in xrange(1, n+1):
            tmp = dp[:]
            for j in xrange(1, k+1):
                tmp[j] = dp[j]-(0 if j < i else dp[j-i])+tmp[j-1]
            dp = tmp
        return (dp[k]-dp[k-1]) % (10**9+7)
    def kInversePairs(self, n, k):
        tmp, dp = [0]*(k+1), [0]*(k+1)
        tmp[0] = dp[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(1, min(k, (i*i-i)/2)+1):
                tmp[j] = tmp[j-1]+dp[j]-(0 if j < i else dp[j-i])
            tmp, dp = dp, tmp
        return dp[-1] % (10**9+7)

    def kInversePairs(self, n, k):
        if not k:
            return 1
        dp, tmp = [1]*(k+1), [1]*(k+1)
        for i in xrange(1, n+1):
            for j in xrange(1, k+1):
                tmp[j] = tmp[j-1]+(dp[j] if j <
                                   i else dp[min(j, (i-2+1)*(i-2)/2)]-dp[j-i])
            dp, tmp = tmp, dp
        return (dp[-1]-dp[-2]) % (10**9+7)

