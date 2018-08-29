# sz1 <= sz2
# k<=sz1+sz2
def findKThIndexes(nums1, nums2, k):
    sz1=len(nums1)
    sz2=len(nums2)
    if sz2==0 or (k<=sz1 and nums1[k-1]<=nums2[0]):
        return (k-1, -1)
    elif sz1==0 or (k<=sz2 and nums2[k-1]<=nums1[0]):
        return (-1, k-1)
    s=0
    e=k-1 if k<sz1 else sz1-1
    while s<=e:
        i=s+(e-s)/2
        j=k-i-2
        if i>=sz1:
            e=i-1
        elif j>=sz2:
            s=i+1
        elif j+1<sz2 and nums1[i]>nums2[j+1]:
            e=i-1
        elif i+1<sz1 and nums2[j]>nums1[i+1]:
            s=i+1
        else:
            return (i,j)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sz1=len(nums1)
        sz2=len(nums2)
        szTotal=sz1+sz2
        if sz2<sz1:
            w=nums1
            nums1=nums2
            nums2=w
        targetSz=int(szTotal/2)+1
        index1, index2=findKThIndexes(nums1, nums2, targetSz)
        if szTotal%2:
            if index1==-1:
                return nums2[index2]
            elif index2==-1:
                return nums1[index1]
            else:
                return nums1[index1] if nums1[index1]>nums2[index2] else nums2[index2]
        else:
            if index1==-1:
                return (nums2[index2]+nums2[index2-1])/2.0
            elif index2==-1:
                return (nums1[index1]+nums1[index1-1])/2.0
            else:
                i=2
                sum=0
                while i:
                    if index2<0 or (index1>=0 and nums1[index1]>nums2[index2]):
                        sum+=nums1[index1]
                        index1-=1
                    else:
                        sum+=nums2[index2]
                        index2-=1
                    i-=1
                return sum/2.0

s=Solution()
print s.findMedianSortedArrays([3], [-2,-1])
