from sys import maxint

class Solution(object):
    def maxValueAfterReverse(self, nums):
        res, minimum, maximum, change = 0, -maxint, maxint, 0
        for i in xrange(0, len(nums)-1):
            a, b = nums[i], nums[i+1]
            res += abs(a-b)
            change = max([change, abs(nums[0]-b)-abs(a-b),
                          abs(nums[-1]-a)-abs(a-b)])
            minimum = max(minimum, min(a, b))
            maximum = min(maximum, max(a, b))
        return res+max(change, (minimum-maximum)*2)

