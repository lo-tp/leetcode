class Solution(object):
    def findComplement(self, num):
        ary=[1<<i for i in range(1, 33)]
        m=[i for i in ary if i > num][0]
        return (m-1)^num

soluction = Solution()
print soluction.findComplement(5)
print soluction.findComplement(1)
