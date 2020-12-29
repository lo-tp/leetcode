class Solution(object):
    def search(self, nums, target):
        s, e = 0, len(nums)-1
        while s <= e:
            if target == nums[e]:
                return True
            else:
                m = s+(e-s)/2
                if nums[m] == target:
                    return True
                elif nums[m] == nums[e]:
                    e -= 1
                elif nums[m] < nums[e] and target > nums[e]:
                    e = m-1
                elif nums[m] > nums[e] and target < nums[e]:
                    s = m+1
                elif nums[m] > target:
                    e = m-1
                else:
                    s = m+1
        return False
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l < r:
            m = int(l+(r-l)/2)
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m
            elif nums[r-1] > nums[r]:
                l = r
            else:
                r -= 1
        nums = nums[l:]+nums[:l]
        l, r = 0, len(nums)-1
        while l <= r:
            m = int(l+(r-l)/2)
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return True
        return False

