from collections import defaultdict


class Solution(object):
    def subarraySumBetter(self, nums, k):
        res, sum, data = 0, 0, defaultdict(lambda : 0)
        data[0]=1
        for num in nums:
            sum += num
            dif = sum-k
            res += data[dif]
            data[sum] += 1
        return res
    def subarraySum(self, nums, k):
        res, sum, data = 0, 0, {0: 1}
        for i in nums:
            sum += i
            if sum-k in data:
                res += data[sum-k]
            if sum in data:
                data[sum] += 1
            else:
                data[sum] = 1
        return res
    def subarraySumTLE(self, nums, k):
        res, size = 0, len(nums)
        for start in xrange(0, size):
            tmp = 0
            for index in xrange(start, size):
                tmp += nums[index]
                if tmp == k:
                    res += 1
        return res
