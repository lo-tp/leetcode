from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(nums[i], i) for i in range(0, len(sz))]
        nums.sort()
        l, r = 0, len(nums) - 1
        while nums[l][0] + nums[r][0] != target:
            if nums[l][0] + nums[r][0] < target:
                l += 1
            else:
                r -= 1
        return [nums[l][1], nums[r][1]]
