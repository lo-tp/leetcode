class Solution(object):
    def findComplement(self, num):
       tem = 1
       while tem<=num:
           tem<<=1
       return tem - 1 - num
soluction = Solution()
print soluction.findComplement(5)
print soluction.findComplement(1)
