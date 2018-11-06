class Solution(object):
    def maxProfit(self, prices):
        size=len(prices)
        buy=[0]*size
        sale=[0]*size
        rest=[0]*size
        if prices:
            buy[0]=-prices[0]
            index=1
            for i in prices[1:]:
                previousIndex=index-1
                buy[index]=max(buy[previousIndex], rest[previousIndex]-i)
                sale[index]=max(buy[previousIndex]+i, sale[previousIndex])
                rest[index]=max(buy[previousIndex], sale[previousIndex], rest[previousIndex])
                index+=1
            # print 'buy', buy
            # print 'sale', sale
            # print 'rest', rest
            return max(buy[-1], sale[-1], rest[-1])
        return 0

s=Solution()
print s.maxProfit([])
print s.maxProfit([123])
print s.maxProfit([1,2,3,0,2])
