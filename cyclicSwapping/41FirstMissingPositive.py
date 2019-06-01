class Solution(object):
    def firstMissingPositive(self, nums):
        index, size = 0, len(nums)
        if size:
            while index < size:
                to_exchange = nums[index]
                while to_exchange > 0 and to_exchange <= size and to_exchange != nums[to_exchange-1]:
                    tmp = nums[to_exchange-1]
                    nums[to_exchange-1] = to_exchange
                    to_exchange = tmp
                index += 1
            index = 0
            while index < size and index+1 == nums[index]:
                index += 1
            return index+1
        return 1
