from collections import defaultdict


class Solution(object):
    def findLHS(self, nums):
        res, data = 0, defaultdict(lambda: 0)
        for num in nums:
            data[num] += 1
        keys = data.keys()
        for i in xrange(0, len(keys)-1):
            if abs(keys[i]-keys[i+1]) == 1:
                res = max(res, data[keys[i]]+data[keys[i+1]])
        return res

