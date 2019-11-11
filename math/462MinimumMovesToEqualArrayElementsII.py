from collections import Counter
from sys import maxint


class Solution(object):
    def minMoves2(self, nums):
        res, data = maxint, sorted(Counter(nums).items(), key=lambda k: k[0])
        r_sum, l_sum, l_size, r_size = sum(
            nums)-data[0][0]*data[0][1], 0, 0, sum([k[1] for k in data[1:]])
        for index in xrange(0, len(data)-1):
            num, size = data[index]
            res = min(res, (num*l_size-l_sum)+(r_sum-r_size*num))
            l_size += size
            l_sum += size*num
            num, size = data[index+1]
            r_size -= size
            r_sum -= size*num
        num, size = data[-1]
        res = min(res, (num*l_size-l_sum)+(r_sum-r_size*num))
        return res
    def minMoves2Better(self, nums):
        size = len(nums)
        nums.sort()
        return sum([abs(k-nums[size/2]) for k in nums])
