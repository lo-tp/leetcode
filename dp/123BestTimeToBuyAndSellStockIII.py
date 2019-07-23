class Solution(object):
    def maxProfit(self, prices):
        res, size = 0, len(prices)
        if size > 1:
            dp = [0]*size
            for _ in xrange(0, 2):
                tmp = dp[0]-prices[0]
                for i in xrange(1, size):
                    tem = max(dp[i-1], tmp+prices[i])
                    tmp = max(tmp, dp[i]-prices[i])
                    dp[i] = tem
                    res = max(tem, res)
        return res
    def maxProfitTLE(self, prices):
        size, res, stack = len(prices), 0, [(0, 0, 0, 2, False)]
        while stack:
            index, holding, profit, residue, bought = stack.pop()
            if index < size:
                stack.append((index+1, holding, profit, residue, bought))
                if bought and prices[index] > holding and residue:
                    tmp = profit+prices[index]-holding
                    res = max(res, tmp)
                    stack.append(
                        (index+1, 0, tmp, residue-1, False))
                elif not holding:
                    stack.append(
                        (index+1, prices[index], profit, residue, True))
        return res
