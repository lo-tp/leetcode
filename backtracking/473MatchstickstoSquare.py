from typing import List
from math import floor

def canDividedIntoK(nums: List[int], k: int):
    total = sum(nums)
    if not total % k:
        nums.sort()
        target = total / k
        if nums[-1] > target:
            return False
        sz = len(nums)
        maxState, bitMask = 1 << sz, [1 << i for i in range(0, sz)]
        dp = [-1] * maxState
        dp[0] = 0
        for state in range(0, maxState):
            if dp[state] >= 0:
                for index in range(0, sz):
                    if dp[state] % target + nums[index] > target:
                        break
                    nextState = state | bitMask[index]
                    if nextState == maxState - 1:
                        return True
                    if dp[nextState] < 0:
                        dp[nextState] = dp[state] + nums[index]
    return False

class Solution:
    def makesquareTLEWithBacktracking(self, matchsticks: List[int]) -> bool:
        sz = sum(matchsticks)
        if sz % 4 or matchsticks[0] * 4 > sz:
            return False
        edges = [floor(sz / 4)] * 4
        stack = [(0, 3, False)]
        while stack:
            # print(edges)
            # print(stack)
            index, edgeIndex, flag = stack.pop()
            if not flag:
                edges[edgeIndex] -= matchsticks[index]
                # if not edges[edgeIndex]:
                # print(index, edgeIndex)
                    # print(edges)
                # print(stack)
                # if not sum(edges):
                if len([e for e in edges if e])==3:
                    return True
                stack.append((index, edgeIndex, True))
                index += 1
                for e in range(0, 4):
                    if edges[e] and edges[e] >= matchsticks[index]:
                        stack.append((index, e, False))
                        break
            else:
                edges[edgeIndex] += matchsticks[index]
                for e in range(edgeIndex + 1, 4):
                    if edges[e] and edges[e] >= matchsticks[index]:
                        stack.append((index, e, False))
                        break
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        return canDividedIntoK(matchsticks, 4)
