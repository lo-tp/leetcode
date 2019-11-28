class Solution(object):
    def singleNumber(self, nums):
        a, b = -0, -0
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
        if b & (1 << 31):
            return - (2 ** 32-b)
        return b
    def singleNumberBetter(self, nums):
        a, b, bits = 0, 0, [1 << i for i in xrange(0, 32)]
        for num in nums:
            for bit in bits:
                if bit & num:
                    if a & bit:
                        a ^= bit
                    elif b & bit:
                        a ^= bit
                        b ^= bit
                    else:
                        b ^= bit
        tmp = 1 << 32
        if b & bits[-1]:
            return -(~b+1)
        return b

    def singleNumberNoNegativeSupport(self, nums):
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


