class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = []
        lIndex, rIndex, lSz, rSz = 0, 0, len(nums1), len(nums2)
        while lIndex < lSz and rIndex < rSz:
            if nums1[lIndex] < nums2[rIndex]:
                arr.append(nums1[lIndex])
                lIndex += 1
            else:
                arr.append(nums2[rIndex])
                rIndex += 1
        while lIndex < lSz:
            arr.append(nums1[lIndex])
            lIndex += 1
        while rIndex < rSz:
            arr.append(nums2[rIndex])
            rIndex += 1
        sz = len(arr)
        if sz % 2:
            return arr[sz/2]
        else:
            return float(arr[sz/2]+arr[sz/2-1])/2

