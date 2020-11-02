class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        if r > 0:
            while l <= r:
                m = l+(r-l)/2
                if nums[m] > nums[m+1]:
                    return nums[m+1]
                elif nums[m-1] > nums[m]:
                    return nums[m]
                elif nums[m] < nums[r]:
                    r = m-1
                elif nums[m] > nums[r]:
                    l = m+1
                elif nums[m] == nums[r]:
                    r -= 1
        return nums[0]
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        if r:
            while l < r:
                if nums[l] < nums[r]:
                    break
                m = l+floor((r-l)/2)
                if nums[m] > nums[m+1]:
                    return nums[m+1]
                elif nums[m-1] > nums[m]:
                    return nums[m]
                elif nums[m] < nums[l]:
                    r = m-1
                elif nums[m] > nums[l]:
                    l = m+1
                elif nums[m] == nums[l]:
                    l += 1
        return nums[l]
