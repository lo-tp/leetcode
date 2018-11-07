class Solution(object):
    def maxCoins(self, nums):
        data=[1]+nums+[1]
        size=len(nums)
        dp=[[0 for i in xrange(0, size+2)] for k in xrange(0, size+2)]
        for i in xrange(1, size+1):
            dp[i][i]=data[i-1]*data[i]*data[i+1]
        for interval in xrange(1, size):
            for startIndex in xrange(1, size+1-interval):
                endIndex=startIndex+interval
                for breakPoint in xrange(startIndex, endIndex+1):
                    dp[startIndex][endIndex]=max(dp[startIndex][endIndex],
                                                 dp[startIndex][breakPoint-1]+dp[breakPoint+1][endIndex]+data[breakPoint]*data[startIndex-1]*data[breakPoint+1])
        return dp[1][size]
s=Solution()
print s.maxCoins([3,1,5,8])
print s.maxCoins([3,1])
print s.maxCoins([3])
print s.maxCoins([])
