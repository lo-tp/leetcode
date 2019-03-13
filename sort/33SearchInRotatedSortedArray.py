from sys import maxint


class Solution:
    def searchClearer(self, nums, target):
        s, e = 0, len(nums)-1
        if e >= 0 and target == nums[e]:
            return e
        e -= 1

        while s <= e:
            m = s+(e-s)/2
            if target < nums[-1] and nums[m] > nums[-1]:
                s = m+1
            elif target > nums[-1] and nums[m] < nums[-1]:
                e = m-1
            elif target < nums[m]:
                e = m-1
            elif target > nums[m]:
                s = m+1
            else:
                return m
        return -1
    def search(self, nums, target):
        s, e = 0, len(nums)-1
        while s <= e:
            m = s+(e-s)/2
            if nums[m] == target:
                return m
            k = nums[m]
            if (nums[m] > nums[-1]) != (target > nums[-1]):
                k = maxint if target > nums[-1] else -maxint
            if k > target:
                e = m-1
            else:
                s = m+1
        return -1
