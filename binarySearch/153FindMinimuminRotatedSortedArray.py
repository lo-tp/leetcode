
class Solution(object):
    def findMin(self, nums):
        sz = len(nums)
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, sz-1
        while l <= r:
            m = l+(r-l)/2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m-1] > nums[m]:
                return nums[m]
            elif nums[m] > nums[0]:
                l = m+1
            elif nums[m] < nums[0]:
                r = m-1
    def findMin(self, nums):
        sz = len(nums)
        if sz == 1 or nums[0] < nums[-1]:
            return nums[0]
        l, r = 1, sz-1
        while l <= r:
            m = l+(r-l)/2
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m+1] < nums[m]:
                return nums[m+1]
            elif nums[m] < nums[0]:
                r = m-1
            elif nums[m] > nums[0]:
                l = m+1
