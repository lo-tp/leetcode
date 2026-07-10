class Solution(object):
    def maxProfit(self, k, prices):
        res, size = 0, len(prices)
        if size > 2:
            dp = [0]*size
            if k > size/2:
                for i in xrange(1, size):
                    if prices[i] > prices[i-1]:
                        res += prices[i]-prices[i-1]
            else:
                for _ in xrange(0, k):
                    tmp = dp[0]-prices[0]
                    for i in xrange(1, size):
                        tem = max(dp[i-1], prices[i]+tmp)
                        tmp = max(tmp, dp[i]-prices[i])
                        res = max(res, tem)
                        dp[i] = tem
        return res

    def maxProfit(self, k: int, prices: List[int]) -> int:
        sz=len(prices)
        if k==0:
            return 0
        if k>=sz//2:
            return sum([max(0, prices[i]-prices[i-1]) for i in range(1,sz)])
        buy,sell=[-float('int')]*k,[0]*k
        for p in prices:
            for idx in range(0,k):
                if idx:
                    buy[idx]=max(buy[idx], sell[idx-1]-p)
                else:
                    buy[idx]=max(buy[idx], -p)
                sell[idx]=max(sell[idx], buy[idx]+p)
        return sell[-1]
