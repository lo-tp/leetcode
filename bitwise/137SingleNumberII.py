class Solution(object):
    def singleNumber(self, nums):
        a, b = 0, 0
        for num in nums:
            for i in xrange(0, 32):
                bit_number = 1 << i
                if num & bit_number:
                    if a & bit_number:
                        a ^= bit_number
                    elif b & bit_number:
                        b ^= bit_number
                        a |= bit_number
                    else:
                        b ^= bit_number
        return b


