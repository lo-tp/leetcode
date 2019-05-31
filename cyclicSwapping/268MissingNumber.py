class Solution(object):
    def missingNumber(self, nums):
        res, index, size = 0, 0, len(nums)
        while index < size:
            scanning_index = nums[index]
            while scanning_index != size and scanning_index != nums[scanning_index]:
                tmp = nums[scanning_index]
                nums[scanning_index] = scanning_index
                scanning_index = tmp
            index += 1
        while res < size and res == nums[res]:
            res += 1
        return res
