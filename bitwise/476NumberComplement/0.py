def helper(k):
    if k is 0:
        return 1
    else:
        return 0
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binaryForm = []
        tem = num
        while tem:
            binaryForm.append(tem%2)
            tem = tem >> 1
        binaryForm.reverse()
        complement=map(helper, binaryForm)
        try:
            index=complement.index(1)
            complement=complement[index:]
            complement.reverse()
            ratio=1
            sum=0
            for i in complement:
                sum+=i*ratio
                ratio*=2
            return sum
        except ValueError:
            return 0
        
soluction = Solution()
print soluction.findComplement(5)
print soluction.findComplement(1)
