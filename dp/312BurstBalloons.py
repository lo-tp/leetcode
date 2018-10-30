class Solution(object):
    def maxCoins(self, nums):
        data=[1]+nums+[1]
        size=len(nums)
        dp= [[0 for i in range(size+2)] for j in range(size+2)]
        for i in xrange(1, size+1):
            dp[i][i]=data[i-1]*data[i]*data[i+1]
        for interval in xrange(1, size):
            for startPos in xrange(1,size-interval+1):
                endPos=startPos+interval
                for breakPoint in xrange(startPos, endPos+1):
                    dp[startPos][endPos]=max(dp[startPos][endPos], data[breakPoint]*data[startPos-1]*data[endPos+1]+dp[startPos][breakPoint-1]+dp[breakPoint+1][endPos])
        return dp[1][size]
s=Solution()
print s.maxCoins([3,1,5,8])
print s.maxCoins([3,1])
print s.maxCoins([3])
print s.maxCoins([])
