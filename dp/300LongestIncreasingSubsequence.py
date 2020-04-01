from sys import maxint
from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1 for i in nums]
        for i in xrange(1, len(nums)):
            for j in xrange(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) if dp else 0

    # time complexity: nlogn
    def lengthOfLISBetter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        if len(nums):
            records = [nums[0]]
            ret += 1
            for x in xrange(1, len(nums)):
                i = nums[x]
                if i > records[-1]:
                    records.append(i)
                    ret += 1
                elif i <= records[0]:
                    records[0] = i
                else:
                    s = 0
                    e = ret-1
                    while s <= e:
                        m = s+(e-s)/2
                        if m == 0 or i > records[m]:
                            s = m+1
                        elif i <= records[m-1]:
                            e = m-1
                        else:
                            records[m] = i
                            break
        return ret

    def lengthOfLISBetter(self, nums):
        dp = [-maxint]
        for i in nums:
            if i > dp[-1]:
                dp.append(i)
            else:
                j = bisect_left(dp, i)
                dp[j] = i
        return len(dp)-1

