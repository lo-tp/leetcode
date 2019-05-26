class Solution(object):
    def find(self, target):
        if target < 0:
            self.dp[target] = 0
        elif target not in self.dp:
            self.dp[target] = 0
            for num in self.nums:
                self.dp[target] += self.find(target-num)
        return self.dp[target]

    def combinationSum4(self, nums, target):
        self.dp, self.nums = {0: 1}, nums
        return self.find(target)

    def combinationSum4WithoutRecursion(self, nums, target):
        dp = {0: 1}
        for i in xrange(0, target):
            if i in dp:
                for num in nums:
                    next = i+num
                    if next in dp:
                        dp[next] += dp[i]
                    else:
                        dp[next] = dp[i]

        return dp[target] if target in dp else 0
