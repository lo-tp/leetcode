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
