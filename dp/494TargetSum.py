class Solution(object):
    def findTargetSumWays(self, nums, S):
        size, total = len(nums), sum(nums)
        upper_limit = total*2+1
        if S > total or S < -total:
            return 0
        dp = [[0]*(upper_limit) for _ in xrange(0, size)]
        dp[0][total-nums[0]] += 1
        dp[0][nums[0]+total] += 1
        for i in xrange(1, size):
            for j in xrange(0, upper_limit):
                if j+nums[i] < upper_limit:
                    dp[i][j] += dp[i-1][j+nums[i]]
                if j-nums[i] > -1:
                    dp[i][j] += dp[i-1][j-nums[i]]
        return dp[size-1][S+total]

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

    def findTargetSumWaysOptimizedBySet(self, nums, S):
        if S > 1000 or S < -1000:
            return 0
        size = len(nums)
        data, dp = set(), [[0]*2001 for _ in xrange(0, size)]
        dp[0][1000+nums[0]] += 1
        dp[0][1000-nums[0]] += 1
        data.add(1000+nums[0])
        data.add(1000-nums[0])
        for i in xrange(1, size):
            positive = [(k-nums[i], k) for k in data if k-nums[i] > -1]
            negative = [(k+nums[i], k) for k in data if k+nums[i] < 2001]
            for j, k in positive:
                dp[i][j] += dp[i-1][k]
                data.add(j)
            for j, k in negative:
                dp[i][j] += dp[i-1][k]
                data.add(j)
        return dp[size-1][S+1000]

    def findTargetSumWaysDoneWithDict(self, nums, S):
        tmp = {0: 1}
        for num in nums:
            tem = defaultdict(lambda: 0)
            for prev in tmp:
                t, te = prev-num, prev+num
                tem[t] += tmp[prev]
                tem[te] += tmp[prev]
            tmp = tem
        return tmp[S]
