class Solution(object):
    def numSquares(self, n):
        dp=[0]*(n+1)
        squares=[]
        index=1
        while index**2<=n:
            square=index**2
            if square==n:
                return 1
            squares.append(square)
            index+=1
        index=1
        while index<=n:
            tmp=map(lambda x:dp[index-x]+1, filter(lambda x:x<=index,squares))
            dp[index]=min(tmp)
            index+=1
        return dp[n]

s=Solution()
print s.numSquares(2)
