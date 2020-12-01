from sys import maxsize


class Solution(object):
    def jump(self, nums):
        sz, dp = len(nums), [maxsize for _ in nums]
        dp[-1] = 0
        for i in range(sz-2, -1, -1):
            for j in range(i+1, min(sz, i+nums[i]+1)):
                dp[i] = min(dp[i], dp[j])
            dp[i] += 1
        return dp[0]
