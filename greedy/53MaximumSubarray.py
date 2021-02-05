class Solution(object):
    def maxSubArray(self, nums):
        res, m = nums[0], nums[0]
        for i in nums[1:]:
            m = max(i, m+i)
            res = max(res, m)
        return res
    def maxSubArray(self, nums):
        res, min_sum, total = nums[0], 0, 0
        for num in nums:
            total += num
            res = max(res, total-min_sum)
            min_sum = min(total, min_sum)
        return res
