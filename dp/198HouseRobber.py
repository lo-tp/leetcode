class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        if size==0:
            return 0
        elif size==1:
            return nums[0]
        else:
            records=[0]*size
            records[0]=nums[0]
            records[1]=max(nums[1],nums[0])
            index=2
            while index<size:
                records[index]=max(records[index-2]+nums[index], records[index-1])
                index+=1
            return max(records[index-1], records[index-2])
    def rob(self, nums):
        dp, sz = nums[:], len(nums)
        if not sz:
            dp = [0]
        elif sz > 2:
            dp.append(0)
            for i in range(sz-3, -1, -1):
                dp[i] = max(dp[i+2], dp[i+3])+nums[i]
        return max(dp)
