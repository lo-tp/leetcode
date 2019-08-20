class Solution(object):
    def singleNonDuplicate(self, nums):
        size = len(nums)
        l, r = 0, size-1
        while True:
            m = l+(r-l)/2
            if not m % 2:
                if m < size-1 and nums[m] == nums[m+1]:
                    l = m+1
                elif m and nums[m] == nums[m-1]:
                    r = m-1
                else:
                    return nums[m]
            else:
                if m and nums[m] == nums[m-1]:
                    l = m+1
                elif m < size-1 and nums[m] == nums[m+1]:
                    r = m-1
                else:
                    return nums[m]

