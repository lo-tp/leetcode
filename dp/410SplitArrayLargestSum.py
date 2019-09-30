class Solution(object):
    def splitArrayWithBinarySearch(self, nums, m):
        l, r = 0, 0
        for num in nums:
            l = max(num, l)
            r += num
        while l <= r:
            mid = l+(r-l)/2
            count, tmp = 1, 0
            for num in nums:
                tmp += num
                if tmp > mid:
                    count += 1
                    tmp = num
                    if count > m:
                        break
            if count > m:
                l = mid+1
            else:
                r = mid-1
        return l

    def splitArray(self, nums, m):
        size = len(nums)
        dp = [[0 for _ in xrange(0, m)] for _ in xrange(0, size)]
        tmp = 0
        for i in xrange(0, size):
            tmp += nums[i]
            dp[i][0] = tmp
        for i in xrange(1, size):
            for j in xrange(1, min(i+1, m)):
                dp[i][j] = min([max(dp[w][j-1], dp[i][0]-dp[w][0])
                                for w in xrange(j-1, i)])
        return dp[size-1][m-1]

    def splitArrayWithDPEasierToUnderstand(self, nums, m):
        size = len(nums)
        dp = [[0 for _ in xrange(0, m)] for _ in xrange(0, size)]
        tmp = 0
        for i in xrange(0, size):
            tmp += nums[i]
            dp[i][0] = tmp

        for w in xrange(1, m):
            for i in xrange(w, size):
                dp[i][w] = min([max(dp[k][w-1], dp[i][0]-dp[k][0]) for k in xrange(w-1,i)])
        return dp[size-1][m-1]

