class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records=dict()
        i=0
        while i<len(nums):
            another=target-nums[i]
            if another in records:
                anotherIndex=records[another]
                return [i,anotherIndex]
            else:
                records[nums[i]]=i
            i+=1
