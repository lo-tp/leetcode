class Solution(object):
    def qc(self, arr, start, end):
        e=end
        s=start
        m=arr[s+(e-s)/2]
        while s<=e:
            while arr[s]<m:
                s+=1
            while arr[e]>m:
                e-=1
            if s<=e:
                if arr[s]!=arr[e]:
                    arr[s]=arr[s]^arr[e]
                    arr[e]=arr[s]^arr[e]
                    arr[s]=arr[s]^arr[e]
                s+=1
                e-=1
        if s<end:
            self.qc(arr, s, end)
        if start<e:
            self.qc(arr, start, e)

    def majorityElement(self, nums):
        self.qc(nums,0,len(nums)-1)
        i=0
        halfSize=len(nums)/2
        while True:
            k=0
            while nums[i]==nums[k+i]:
                k+=1
                if k>halfSize:
                    return nums[i]
            i+=k

    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records=dict()
        halfSize=len(nums)/2
        for i in nums:
            if i in records:
                appearanceTime=records[i]+1
                if appearanceTime>halfSize:
                    return i
                records[i]+=1
            else:
                appearanceTime=+1
                if appearanceTime>halfSize:
                    return i
                records[i]=1
