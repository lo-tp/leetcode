from heapq import heappush, heappop, heapify


def heapify(arr):
    size = len(arr)
    if size > 1:
        index = (size-2)/2
        while index >= 0:
            mIndex = index*2+1
            rightIndex = mIndex+1
            if rightIndex < size and arr[rightIndex] < arr[mIndex]:
                mIndex = rightIndex
            if mIndex < size and arr[mIndex] < arr[index]:
                arr[mIndex], arr[index] = arr[index], arr[mIndex]
            index -= 1


class Solution(object):
    def findKthLargest(self, nums, k):
        first = nums[:k]
        heapify(first)
        for i in nums[k:]:
            if i > first[0]:
                first[0] = i
                heapify(first)
        return first[0]


class Solution(object):
    def findKthLargest(self, nums, k):
        data = []
        k = len(nums)-k+1
        for i in range(0, k):
            data.append(-nums[i])
        heapify(data)
        for j in range(k, len(nums)):
            if -nums[j] > data[0]:
                heappop(data)
                heappush(data, -nums[j])
        return -data[0]


s = Solution()
