class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if not total % 2:
            sz, target = len(nums), int(total/2)
            dp = [False]*(target+1)
            dp[0] = True
            for i in range(0, sz):
                tmp = [False]*(target+1)
                tmp[0] = True
                for j in range(0, target+1):
                    if dp[j]:
                        tmp[j] = True
                        if j+nums[i] <= target:
                            tmp[j+nums[i]] = True
                dp = tmp
            return dp[-1]
        return False
