class Solution(object):
    def productExceptSelf(self, nums):
        size=len(nums)
        ret=[1]*size
        right=1
        left=1
        for x in xrange(0,size):
            rIndex=size-1-x
            tmp=nums[rIndex]
            ret[rIndex]=right
            right*=tmp
        for x in xrange(0,size):
            ret[x]*=left
            left*=nums[x]
        return ret

s=Solution()
print s.productExceptSelf( [1,2])
