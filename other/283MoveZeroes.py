class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        l=len(nums)-1
        while i<l:
            while i<l and nums[i]!=0:
                i+=1
            k=i+1
            while k<=l and nums[k]==0:
                k+=1
            if i<l and k<=l:
                nums[i]=nums[i]^nums[k]
                nums[k]=nums[i]^nums[k]
                nums[i]=nums[i]^nums[k]
            i+=1
