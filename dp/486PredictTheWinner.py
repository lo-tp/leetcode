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
