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
