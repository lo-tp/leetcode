def heapify(arr):
    size=len(arr)
    if size>1:
        index=(size-2)/2
        while index>=0:
            mIndex=index*2+1
            rightIndex=mIndex+1
            if rightIndex<size and arr[rightIndex]<arr[mIndex]:
                mIndex=rightIndex
            if mIndex<size and arr[mIndex]<arr[index]:
                arr[mIndex],arr[index]=arr[index], arr[mIndex]
            index-=1

class Solution(object):
    def findKthLargest(self, nums, k):
        first=nums[:k]
        heapify(first)
        for i in nums[k:]:
            if i>first[0]:
                first[0]=i
                heapify(first)
        return first[0]

s=Solution()
print s.findKthLargest([3,2,1,5,6,4],2)
