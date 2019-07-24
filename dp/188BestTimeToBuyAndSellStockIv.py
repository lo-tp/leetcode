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

