class Solution(object):
    def calculate(self, arr, index):
        if index == self.size:
            self.ret.append([i for i in arr])
        else:
            arr.append(self.nums[index])
            self.calculate(arr, index+1)
            arr.pop()
            self.calculate(arr, index+1)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret=[]
        if len(nums):
            self.nums=nums
            self.size=len(nums)
            self.calculate([], 0)
        return self.ret
