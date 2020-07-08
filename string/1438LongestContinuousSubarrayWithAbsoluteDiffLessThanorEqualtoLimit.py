class Solution(object):
    def longestSubarray(self, nums, limit):
        minimum, maximum, l, res = nums[0], nums[0], 0, 0
        for r in xrange(0, len(nums)):
            maximum = max(maximum, nums[r])
            minimum = min(minimum, nums[r])
            if maximum-minimum > limit:
                while l <= r:
                    l += 1
                    t = nums[l:r+1]
                    maximum, minimum = max(t), min(t)
                    if maximum-minimum <= limit:
                        break
            res = max(r-l+1, res)
        return res
