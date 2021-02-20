from typing import List
from collections import defaultdict


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        sz, res = len(coins), 0
        if amount:
            current, stack = 0, [(t, False) for t in range(0, sz)]
            while stack:
                t, flag = stack.pop()
                if flag:
                    if current == amount:
                        res += 1
                    current -= coins[t]
                elif current < amount:
                    current += coins[t]
                    stack.append((t, True))
                    stack.extend([(i, False) for i in range(t, sz)])
        else:
            res = 1
        return res
