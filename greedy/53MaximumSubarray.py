class Solution(object):
    def maxSubArray(self, nums):
        res, m = nums[0], nums[0]
        for i in nums[1:]:
            m = max(i, m+i)
            res = max(res, m)
        return res
