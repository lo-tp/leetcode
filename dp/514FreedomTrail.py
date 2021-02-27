from collections import defaultdict
from sys import maxsize


class Solution(object):
    def findRotateSteps(self, ring, key):
        r_sz, k_sz = len(ring), len(key)
        stack, data, dp = [(0, 0, 0)], defaultdict(
            lambda: []), [maxsize]*(k_sz)
        for index, k in enumerate(ring):
            data[k].append(index)
        while stack:
            cur, target, cur_step = stack.pop()
            if target < k_sz:
                for index in data[key[target]]:
                    move_step = abs(cur-index)
                    move_step = min(move_step, r_sz-move_step)
                    new_cur_step = move_step+1+cur_step
                    dp[target] = min(new_cur_step, dp[target])
                    stack.append((index, target+1, new_cur_step))
        return dp[-1]
    def findRotateSteps(self, ring, key):
        data, r_sz, k_sz = defaultdict(lambda: []), len(ring), len(key)
        stack, dp = [(0, 0, False)], defaultdict(lambda: maxsize)
        for index, k in enumerate(ring):
            data[k].append(index)
            if k == key[-1]:
                dp[(index, k_sz)] = 0
        while stack:
            cur_r, cur_k, flag = stack.pop()
            if flag:
                for index in data[key[cur_k]]:
                    step = abs(cur_r-index)
                    step = min(step, r_sz-step)
                    dp[(cur_r, cur_k)] = min(
                        dp[(cur_r, cur_k)], step+1+dp[(index, cur_k+1)])
            elif dp[(cur_r, cur_k)] == maxsize:
                stack.append((cur_r, cur_k, True))
                stack.extend([(index, cur_k+1, False)
                              for index in data[key[cur_k]]])
        return dp[(0, 0)]
