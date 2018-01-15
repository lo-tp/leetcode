def isSelfDivisible(n):
    duplication = n
    while duplication:
        remainder = duplication % 10
        if remainder is 0:
            return False
        if n % remainder is not 0:
            return False
        duplication = (duplication - remainder)/10
    return True

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        index = left
        while index<=right:
            if isSelfDivisible(index):
                result.append(index)
            index+=1
        return result

soluction = Solution()
print soluction.selfDividingNumbers(1,22)
