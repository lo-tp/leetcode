class Solution(object):
    def findMaxAverage(self, nums, k):
        res = 0
        for i in nums[:k]:
            res += i
        tmp = res
        for i in xrange(k, len(nums)):
            tmp += nums[i]-nums[i-k]
            res = max(res, tmp)
        return float(res)/k
