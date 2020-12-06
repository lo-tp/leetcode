from sys import maxsize


class Solution(object):
    def jump(self, nums):
        sz, dp = len(nums), [maxsize for _ in nums]
        dp[-1] = 0
        for i in range(sz-2, -1, -1):
            for j in range(i+1, min(sz, i+nums[i]+1)):
                dp[i] = min(dp[i], dp[j])
            dp[i] += 1
        return dp[0]

    def jump(self, nums):
        cur, jump, next_bound, sz = 1, 0, nums[0], len(nums)
        while cur < sz:
            bound = next_bound
            while cur <= bound and cur < sz:
                next_bound = max(next_bound, cur+nums[cur])
                cur += 1
            jump += 1
        return jump
