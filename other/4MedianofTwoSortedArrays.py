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

    def findMedianSortedArraysBetter(self, nums1, nums2):
        arr = []
        lIndex, rIndex, lSz, rSz = 0, 0, len(nums1), len(nums2)
        sz = (lSz+rSz)/2+1
        while sz and lIndex < lSz and rIndex < rSz:
            if nums1[lIndex] < nums2[rIndex]:
                arr.append(nums1[lIndex])
                lIndex += 1
            else:
                arr.append(nums2[rIndex])
                rIndex += 1
            sz -= 1
        while sz and lIndex < lSz:
            arr.append(nums1[lIndex])
            lIndex += 1
            sz -= 1
        while sz and rIndex < rSz:
            arr.append(nums2[rIndex])
            rIndex += 1
            sz -= 1
        if (lSz+rSz) % 2:
            return arr[-1]
        else:
            return float((arr[-1]+arr[-2]))/2
