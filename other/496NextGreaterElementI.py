from collections import defaultdict


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        data, stack = defaultdict(lambda: -1), []
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                data[num] = stack[-1]
            stack.append(num)
        return [data[num] for num in nums1]
