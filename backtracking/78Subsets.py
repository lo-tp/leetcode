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
    def subsets(self, nums):
        sz, res = len(nums), [[]]
        stack = [[i] for i in xrange(0, sz)]
        while stack:
            t = stack.pop()
            res.append([nums[i] for i in t])
            for i in xrange(t[-1]+1, sz):
                j = t[:]
                j.append(i)
                stack.append(j)
        return res
