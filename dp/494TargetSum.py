class Solution(object):
    def calculate(self, index, sum):
        if sum < 0 or sum > 2000:
            return 0
        if self.memo[index][sum] == -1:
            if index:
                self.memo[index][sum] = self.calculate(
                    index-1, sum+self.nums[index])+self.calculate(index-1, sum-self.nums[index])
            else:
                self.memo[index][sum] = 0
        return self.memo[index][sum]

    def findTargetSumWays(self, nums, S):
        if S >= -1000 and S <= 1000:
            self.size = len(nums)
            self.nums = nums
            self.memo = [[-1]*2001 for _ in xrange(0, self.size)]
            if nums[0]:
                self.memo[0][1000+nums[0]] = 1
                self.memo[0][1000-nums[0]] = 1
            else:
                self.memo[0][1000] = 2
            self.calculate(self.size-1, S+1000)
            return self.calculate(self.size-1, S+1000)
        return 0

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
