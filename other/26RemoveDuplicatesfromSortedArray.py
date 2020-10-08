class Solution(object):
    def removeDuplicates(self, nums):
        sz, res = len(nums), 0
        if sz:
            l, r, res = 1, 1, 1
            while r < sz:
                if nums[r] != nums[r-1]:
                    nums[l] = nums[r]
                    l += 1
                    res += 1
                r += 1
        return res
