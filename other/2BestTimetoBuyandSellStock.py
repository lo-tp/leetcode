from sys import maxint

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        minPrice=maxint
        for i in prices:
            tmp=i-minPrice
            if tmp>profit:
                profit=tmp
            if i<minPrice:
                minPrice=i
        return profit
