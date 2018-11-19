class Solution(object):
    def getScore(self, arr, start, end):
        score=0
        if start in self.dp:
            if end in self.dp[start]:
                return self.dp[start][end]
        else:
            self.dp[start]={}
        if start==end:
            score=arr[start]
        else:
            lScore=arr[start]-self.getScore(arr, start+1, end)
            rScore=arr[end]-self.getScore(arr, start, end-1)
            score=max(lScore, rScore)
        self.dp[start][end]=score
        return score
    def PredictTheWinner(self, nums):
        size=len(nums)
        self.dp={}
        return self.getScore(nums,0,len(nums)-1)>=0

    def PredictTheWinnerWithoutRecursion(self, nums):
        sz=len(nums)
        dp=[[nums[i] if i==k else 0 for i in xrange(0, sz)] for k in xrange(0,sz)]
        for interval in xrange(1, sz):
            for start in xrange(0, sz-interval):
                end=start+interval
                dp[start][end]=max(nums[start]-dp[start+1][end], nums[end]-dp[start][end-1])
        return dp[0][sz-1]>=0 if sz else true

    def PredictTheWinnerWithoutRecursionUseLessSpace(self, nums):
        sz=len(nums)
        dp=nums[:]
        for interval in xrange(1,sz):
            for startPos in xrange(0, sz-interval):
                endPos=startPos+interval
                dp[startPos]=max(nums[endPos]-dp[startPos], nums[startPos]-dp[startPos+1])
        return dp[0]>=0 if sz >0 else True
