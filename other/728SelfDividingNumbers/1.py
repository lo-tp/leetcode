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
    def __init__(self):
        self.data=[False]
        index=1
        for index in range(1, 10001):
            if isSelfDivisible(index):
                self.data.append(True)
            else:
                self.data.append(False)

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for index in range(left, right+1):
            if self.data[index]:
                result.append(index)
        return result

soluction = Solution()
print soluction.selfDividingNumbers(1,22)
