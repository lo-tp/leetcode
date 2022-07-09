from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total, sz, remaining = sum(nums), len(nums), [True]*16
        if not total % k:
            used, cur, target, stack = 0, 0, total/k, [(0, False)]
            while stack:
                index, flag = stack.pop()
                if flag:
                    used -= 1
                    cur -= nums[index]
                    if cur < 0:
                        cur += target
                    remaining[index] = True
                else:
                    stack.append((index, True))
                    remaining[index] = False
                    used += 1
                    cur += nums[index]
                    if cur < target:
                        stack.extend([(i, False)
                                      for i in range(index+1, sz) if remaining[i]])
                    elif cur == target:
                        cur = 0
                        # print(stack)
                        # print('hello')
                        if used == sz:
                            return True
                        for i in range(0, sz):
                            if remaining[i]:
                                stack.append((i, False))
                                break
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if not total % k:
            nums.sort()
            target = floor(total / k)
            if nums[-1] <= target:
                sz = len(nums)
                maxState, bitMask = (1 << sz) - 1, [1 << i for i in range(0, sz)]
                dp = [-1] * (maxState + 1)
                dp[0] = 0
                for state in range(0, maxState + 1):
                    if dp[state] != -1:
                        for j in range(0, sz):
                            if not (bitMask[j] & state):
                                t = dp[state] + nums[j]
                                if t > target:
                                    continue
                                dp[state | bitMask[j]] = t % target
                return not dp[maxState]
        return False

