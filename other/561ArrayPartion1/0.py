class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums)/2):
            result+=nums[i*2]
        return result

soluction = Solution()
print soluction.arrayPairSum([1,4,3,2])
