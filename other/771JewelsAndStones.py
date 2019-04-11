class Solution(object):
    def numJewelsInStones(self, J, S):
        res, dp = 0, {}
        for i in J:
            dp[i] = 0
        for i in S:
            if i in dp:
                res += 1
        return res
