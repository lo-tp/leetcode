from sys import maxint
class Solution(object):
    def maxProfit(self, prices, fee):
        toBuy, toSell=0, -maxint
        for price in prices:
            toBuy, toSell=max(toBuy, toSell+price-fee), max(toSell, toBuy-price)
        return max(toSell, toBuy)
s=Solution()
print s.maxProfit([1,3,7,5,10,3],3)
