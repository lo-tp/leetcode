class Solution(object):
    def calculate(self, arr):
        if len(arr)==len(self.nums):
            self.data.append(arr)
        for i in self.nums:
            if not i in arr:
                tmp=arr[0:]
                tmp.append(i)
                self.calculate(tmp)
    def permute(self, nums):
        self.nums=nums
        self.data=[]
        self.calculate([])
        return self.data
s=Solution()
print s.permute([1,2,3])
