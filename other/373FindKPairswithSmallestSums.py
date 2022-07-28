from typing import List, Optional
from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        sz1, sz2 = len(nums1), len(nums2)
        switched = False
        if sz1 > sz2:
            sz1, sz2, nums1, nums2 = sz2, sz1, nums2, nums1
            switched = True
        index = [0] * sz1
        heap = [(nums1[i] * nums2[0], i) for i in range(0, sz1)]
        res = []
        while heap and k:
            k -= 1
            _, i = heappop(heap)
            res.append(
                (nums2[index[i]], nums1[i]) if switched else (nums1[i], nums2[index[i]])
            )
            index[i] += 1
            if index[i] < sz2:
                heappush(heap, (nums1[i] * nums2[index[i]], i))
        return res
