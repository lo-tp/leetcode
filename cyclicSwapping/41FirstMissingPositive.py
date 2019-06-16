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
    def firstMissingPositiveBetter(self, nums):
        nums.append(-1)
        index, size = 0, len(nums)
        while index < size:
            if nums[index] > 0 and nums[index] != index:
                tmp = nums[index]
                while tmp >= 0 and tmp < size and nums[tmp] != tmp:
                    tem = nums[tmp]
                    nums[tmp] = tmp
                    tmp = tem
            index += 1
        for i in xrange(1, size):
            if i != nums[i]:
                return i
        return size if size else 1
