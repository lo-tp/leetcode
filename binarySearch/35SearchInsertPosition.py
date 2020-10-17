class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l+(r-l)/2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return l
