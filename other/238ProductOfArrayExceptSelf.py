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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sz=len(nums)
        zero_count=0
        zero_idx=-1
        t=1
        for idx,n in enemerate(nums):
            if not n:
                zero_count+=1
                zero_idx=idx
        if zero_count>1:
            return [0]*sz
        if zero_count:
            for n in nums:
                t*=n if n else 1
            return [t if idx==zero_idx else 0 for idx in range(0,sz)]
        res=[]
        for idx in range(0, sz-1):
            t*=nums[idx]
        for idx in range(0,sz-1):
            res.append(t/nums[idx]*nums[-1])
        res.append(t)
        return res

s=Solution()
print s.productExceptSelf( [1,2])
