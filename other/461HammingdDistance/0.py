class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tem=x^y
        i=0
        while tem:
           i+=1
           tem=tem&(tem-1)
        return i
