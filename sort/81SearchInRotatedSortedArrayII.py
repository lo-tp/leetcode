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
