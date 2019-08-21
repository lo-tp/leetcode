class Solution(object):
    def findTargetSumWaysTLE(self, nums, S):
        stack, res = [(len(nums)-1, S)], 0
        while stack:
            index, residue = stack.pop()
            if not residue and index == -1:
                res += 1
            elif index > -1:
                stack.append((index-1, residue+nums[index]))
                stack.append((index-1, residue-nums[index]))
        return res
