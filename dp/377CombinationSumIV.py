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

