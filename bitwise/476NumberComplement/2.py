class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i *= 2
        return (i-1)^num

soluction = Solution()
print soluction.findComplement(5)
print soluction.findComplement(1)
