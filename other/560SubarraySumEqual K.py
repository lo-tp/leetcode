class Solution(object):
    def subarraySum(self, nums, k):
        res, size = 0, len(nums)
        for start in xrange(0, size):
            tmp = 0
            for index in xrange(start, size):
                tmp += nums[index]
                if tmp == k:
                    res += 1
        return res
