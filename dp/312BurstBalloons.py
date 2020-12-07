class Solution(object):
    def maxCoins(self, nums):
        data = [1]+nums+[1]
        sz = len(nums)
        dp = [[0 for i in xrange(0, sz+2)]for k in xrange(0, sz+2)]
        for i in xrange(1, sz+1):
            dp[i][i] = data[i-1]*data[i]*data[i+1]
        for interval in xrange(1, sz):
            for startIndex in xrange(1, sz - interval+1):
                endIndex = startIndex+interval
                for lastIndex in xrange(startIndex, endIndex+1):
                    dp[startIndex][endIndex] = max(dp[startIndex][endIndex], dp[startIndex][lastIndex-1] +
                                                   dp[lastIndex+1][endIndex]+data[startIndex-1]*data[lastIndex]*data[endIndex+1])
        return dp[1][sz] if sz else 0


s = Solution()
