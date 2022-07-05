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
            sz = len(nums)
            target = floor(total / k)
            nums.sort()
            if nums[-1] > target:
                return False
            maxState = 1 << sz
            dp = [-1] * (maxState)
            dp[0] = 0
            bitMask = [1 << i for i in range(0, sz)]
            total, stack = 0, [0, 0]
            for state in range(0, maxState):
                if dp[state] >= 0:
                    for index in range(0, sz):
                        if dp[state] % target + nums[index] <= target:
                            nextState = state | bitMask[index]
                            if nextState == maxState - 1:
                                return True
                            if dp[nextState] == -1:
                                dp[nextState] = dp[state] + nums[index]
                        else:
                            break
        return False
