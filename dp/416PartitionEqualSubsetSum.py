from typing import List

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
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if not target % 2:
            target = int(target/2)
            dp, tmp = [False]*(target+1), [False]*(target+1)
            dp[0] = tmp[0] = True
            for num in nums:
                for i in range(1, target+1):
                    te = i-num
                    tmp[i] = dp[i] or (te >= 0 and dp[te])
                tmp, dp = dp, tmp
            return dp[-1]
        return False
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if not total % 2:
            target, data = total/2, set()
            data.add(0)
            for num in nums:
                te = set()
                for t in data:
                    te.add(num+t)
                data |= te
                if target in data:
                    return True
        return False
