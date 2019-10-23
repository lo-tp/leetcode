class Solution(object):
    def arrangeCoins(self, n):
        res, total = 0, 1
        while total <= n:
            res += 1
            total += res+1
        return res

