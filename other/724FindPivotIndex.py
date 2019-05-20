class Solution(object):
    def pivotIndex(self, nums):
        size, index, left_sum, right_sum, res = len(nums), 0, 0, 0, -1
        for i in nums:
            right_sum += i
        while index < size:
            right_sum -= nums[index]
            if left_sum == right_sum:
                res = index
                break
            left_sum += nums[index]
            index += 1
        return res
