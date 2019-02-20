class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        lSz, s, e = (m+n+1)/2, 0, m
        while s <= e:
            i = s+(e-s)/2
            j = lSz-i
            if i > 0 and nums2[j] < nums1[i-1]:
                e = i-1
            elif i < m and nums1[i] < nums2[j-1]:
                s = i+1
            else:
                lMax, rMin = 0, 0
                if i == 0:
                    lMax = nums2[j-1]
                elif j == 0:
                    lMax = nums1[i-1]
                else:
                    lMax = max(nums2[j-1], nums1[i-1])
                if (m+n) % 2:
                    return lMax
                if i == m:
                    rMin = nums2[j]
                elif j == n:
                    rMin = nums1[i]
                else:
                    rMin = min(nums2[j], nums1[i])
                return float(rMin+lMax)/2


s = Solution()
print s.findMedianSortedArrays([1], [])
print s.findMedianSortedArrays([1, 2], [])
print s.findMedianSortedArrays([1, 2], [3])
print s.findMedianSortedArrays([1, 2], [3, 4])
print s.findMedianSortedArrays([1], [2, 3, 4, 5])
