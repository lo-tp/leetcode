class Solution(object):
    def maxProductTLE(self, nums):
        sz = len(nums)
        dp, res = [1]*sz, nums[0]
        for i in xrange(0, sz):
            lastIndex = sz-i
            for k in xrange(0, lastIndex):
                dp[k] *= nums[k+i]
                res = max(dp[k], res)
        return res
    def maxProduct(self, nums):
        r, prevMax, prevMin = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            if i < 0:
                prevMax, prevMin = prevMin, prevMax
            prevMax = max(prevMax*i, i)
            prevMin = min(prevMin*i, i)
            r = max(r, prevMax)
        return r
