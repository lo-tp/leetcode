class Solution(object):
    def findRecursively(self, sum, index):
        if index==self.size:
            if sum==self.target:
                return 1
            else:
                return 0
        else:
            if sum not in self.records[index]:
                self.records[index][sum]=self.findRecursively(sum+self.nums[index],index+1)+self.findRecursively(sum-self.nums[index], index+1)
            return self.records[index][sum]



    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.nums=nums
        self.size=len(nums)
        self.records=dict()
        for i in xrange(self.size):
            self.records[i]=dict()
        self.result=0
        self.target=S
        return self.findRecursively(0, 0)

s=Solution()
print s.findTargetSumWays([10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46],45)
