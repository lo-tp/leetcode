class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l+(r-l)/2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        return -1

    def search(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            return -1

