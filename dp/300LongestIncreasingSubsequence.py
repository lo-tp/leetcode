class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records=[]
        max=0
        size=len(nums)
        if size:
            max=1
            records.append((1,nums[0]))
            for i in xrange(1, size):
                currentMax=1
                for (previousMax, previousNumber) in records:
                    if previousMax>=currentMax and nums[i]>previousNumber:
                        currentMax=previousMax+1
                if currentMax>max:
                    max=currentMax
                records.append((currentMax, nums[i]))
        return max
