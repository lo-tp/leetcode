class Solution(object):
    def splitArray(self, nums, m):
        size = len(nums)
        dp = [[0 for _ in xrange(0, m)] for _ in xrange(0, size)]
        tmp = 0
        for i in xrange(0, size):
            tmp += nums[i]
            dp[i][0] = tmp
        for i in xrange(1, size):
            for j in xrange(1, min(i+1, m)):
                dp[i][j] = min([max(dp[w][j-1], dp[i][0]-dp[w][0])
                                for w in xrange(j-1, i)])
        return dp[size-1][m-1]

