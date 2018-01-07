class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        ret = 0
        while z:
            w = z & 1
            z = z >> 1
            if w:
                ret += 1
        return ret

soluction = Solution()
print soluction.hammingDistance(2,2)
