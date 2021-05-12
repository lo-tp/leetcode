class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, t = 0, prices[0]
        for p in prices:
            res = max(res, p-t)
            t = min(p, t)
        return res
