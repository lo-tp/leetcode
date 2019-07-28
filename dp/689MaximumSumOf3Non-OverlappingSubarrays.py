class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        size = len(nums)
        data = []
        sum = 0
        for i in xrange(0, k-1):
            sum += nums[i]
        for index, i in enumerate(nums[k-1: size]):
            sum += i
            data.append((index, sum))
            sum -= nums[index]
        m_start, m_end = k, len(data)-k-1
        dp = [[0, data[i][0], 0, data[i][1]] for i in xrange(m_start, m_end+1)]
        index = max_index = len(data)-1
        for i in xrange(len(dp)-1, -1, -1):
            dp[i][3] += data[max_index][1]
            dp[i][2] = data[max_index][0]
            index -= 1
            if data[index][1] >= data[max_index][1]:
                max_index = index
        index = max_index = 0
        for i in xrange(0, len(dp)):
            dp[i][3] += data[max_index][1]
            dp[i][0] = data[max_index][0]
            index += 1
            if data[index][1] > data[max_index][1]:
                max_index = index
        max_index = 0
        for i in xrange(1, len(dp)):
            if dp[i][3] > dp[max_index][3]:
                max_index = i
        return dp[max_index][0:3]
