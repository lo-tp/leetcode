def calculateScore(nums, s, e, add):
    if s==e:
        return nums[s] if add else -nums[s]
    a=calculateScore(nums, s+1, e, not add)
    b=calculateScore(nums, s, e-1, not add)
    if add:
        return max(a+nums[s], b+nums[e])
    else:
        return min(a-nums[s], b-nums[e])


class Solution(object):
    def calculateData(self, nums, s, e):
        if s==e:
            return nums[s]
        if self.dp[s][e]:
            return self.dp[s][e]
        self.dp[s][e]=max(nums[s]-self.calculateData(nums, s+1, e),
                          nums[e]-self.calculateData(nums, s, e-1))
        return self.dp[s][e]
        
    def PredictTheWinner0(self, nums):
        return calculateScore(nums, 0, len(nums)-1, True)>=0
    def PredictTheWinner(self, nums):
        size=len(nums)+1
        self.dp=[[0 for k in xrange(0, size)]for i in xrange(0, size)]
        return self.calculateData(nums, 0, len(nums)-1)>=0

s=Solution()
print s.PredictTheWinner([1, 5, 2])
print s.PredictTheWinner([1, 5, 233, 7])
print s.PredictTheWinner([1163573,4225123,1034109,6416120,4401957,408968,8769389,7498770,6003151,2054050,2621821,8204739,2586055,6520977,2014732,4750306,4172182,6965656,1861876,9549339])
