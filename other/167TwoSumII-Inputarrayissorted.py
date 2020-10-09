class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while True:
            t = nums[l]+nums[r]
            if t == target:
                return [l+1, r+1]
            elif t < target:
                l += 1
            else:
                r -= 1
