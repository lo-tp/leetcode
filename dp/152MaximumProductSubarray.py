class Solution(object):
    def maxProduct(self, nums):
        sz = len(nums)
        dp, res = [1]*sz, nums[0]
        for i in xrange(0, sz):
            lastIndex = sz-i
            for k in xrange(0, lastIndex):
                dp[k] *= nums[k+i]
                res = max(dp[k], res)
        return res
