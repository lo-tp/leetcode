from sys import maxint
import heapq


class Heap():
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def sort(self):
        if self.data > 1:
            index = (self.size-2)/2
            while index >= 0:
                min_index = index*2+1
                right_index = min_index+1
                if right_index < self.size and self.data[right_index][0] < self.data[min_index][0]:
                    min_index = right_index
                if self.data[min_index][0] < self.data[index][0]:
                    self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
                index -= 1

    def get(self):
        res = self.data[0]
        self.size -= 1
        if self.size >= 0:
            self.data[0] = self.data[self.size]
        return res

    def add(self, element):
        self.data[self.size] = element
        self.size += 1

    def isEmpty(self):
        return not self.size


def merge(first, second):
    res, size_1, size_2, index_1, index_2 = [], len(first), len(second), 0, 0
    while index_1 < size_1 and index_2 < size_2:
        if first[index_1] < second[index_2]:
            res.append(first[index_1])
            index_1 += 1
        else:
            res.append(second[index_2])
            index_2 += 1
    while index_1 < size_1:
        res.append(first[index_1])
        index_1 += 1
    while index_2 < size_2:
        res.append(second[index_2])
        index_2 += 1

    return res


class Solution(object):
    def smallestRange(self, nums):
        nums = [k for k in nums if len(k)]
        remaining_num, data, start, end, head, tail, merged = len(
            nums), {}, 0, 0, 0, maxint, []

        for i in nums:
            merged = merge(merged, i)
        merged_size, record = len(
            merged), [0 for i in xrange(0, remaining_num)]

        for index, inner_list in enumerate(nums):
            tmp = set(inner_list)
            for num in tmp:
                if num in data:
                    data[num].append(index)
                else:
                    data[num] = [index]

        while True:
            while remaining_num and end < merged_size:
                num = merged[end]
                for index in data[num]:
                    if not record[index]:
                        remaining_num -= 1
                    record[index] += 1
                end += 1
            if remaining_num:
                break

            while not remaining_num and start < end:
                if merged[end-1]-merged[start] < tail-head:
                    tail, head = merged[end-1], merged[start]
                num = merged[start]
                for index in data[num]:
                    record[index] -= 1
                    if not record[index]:
                        remaining_num += 1
                start += 1
        return [head, tail]


    def smallestRangeBetter(self, nums):
        nums = [k for k in nums if len(k)]
        remaining_num, data, start, end, head, tail, merged = len(
            nums), {}, 0, 0, 0, maxint, []
        heap = Heap([(x[0], index) for index, x in enumerate(nums)])
        indexes = [1 for _ in nums]
        while remaining_num:
            heap.sort()
            num, index = heap.get()
            merged.append(num)
            if indexes[index] != len(nums[index]):
                heap.add((nums[index][indexes[index]], index))
                indexes[index] += 1
            else:
                remaining_num -= 1

        remaining_num = len(nums)
        while not heap.isEmpty():
            merged.append(heap.get()[0])
        merged_size, record = len(
            merged), [0 for _ in xrange(0, remaining_num)]

        for index, inner_list in enumerate(nums):
            tmp = set(inner_list)
            for num in tmp:
                if num in data:
                    data[num].append(index)
                else:
                    data[num] = [index]

        while True:
            while remaining_num and end < merged_size:
                num = merged[end]
                for index in data[num]:
                    if not record[index]:
                        remaining_num -= 1
                    record[index] += 1
                end += 1
            if remaining_num:
                break

            while not remaining_num and start < end:
                if merged[end-1]-merged[start] < tail-head:
                    tail, head = merged[end-1], merged[start]
                num = merged[start]
                for index in data[num]:
                    record[index] -= 1
                    if not record[index]:
                        remaining_num += 1
                start += 1
        return [head, tail]



class MaxHeap():
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def sort(self):
        if self.data > 1:
            index = (self.size-2)/2
            while index >= 0:
                max_index = index*2+1
                right_index = max_index+1
                if right_index < self.size and self.data[right_index][0] > self.data[max_index][0]:
                    max_index = right_index
                if self.data[max_index][0] > self.data[index][0]:
                    self.data[index], self.data[max_index] = self.data[max_index], self.data[index]
                index -= 1

    def get(self):
        res = self.data[0]
        self.size -= 1
        if self.size >= 0:
            self.data[0] = self.data[self.size]
        return res

    def add(self, element):
        self.data[self.size] = element
        self.size += 1


class Solution(object):
    def smallestRangeWithOfficialSolution(self, nums):
        nums = [k for k in nums if len(k)]
        start, end = 0, maxint
        if len(nums):
            end_data = [(x[-1], index, len(x)-1)
                        for index, x in enumerate(nums)]
            min_num = min([x[0] for x in end_data])
            heap = MaxHeap(end_data)
            while True:
                heap.sort()
                max_num, outter_index, inner_index = heap.get()
                if max_num-min_num <= end-start:
                    start, end = min_num, max_num
                if not inner_index:
                    return [start, end]
                inner_index -= 1
                heap.add((nums[outter_index][inner_index],
                          outter_index, inner_index))
                min_num = min(min_num, nums[outter_index][inner_index])



class Solution(object):
    def smallestRangeWithBuiltInHeap(self, nums):
        nums = [k for k in nums if len(k)]
        start, end = 0, maxint
        if len(nums):
            heap = [(x[0], index, 0)
                    for index, x in enumerate(nums)]
            max_num = max([x[0] for x in heap])
            heapq.heapify(heap)
            while True:
                min_num, outter_index, inner_index = heapq.heappop(heap)
                if max_num-min_num < end-start:
                    start, end = min_num, max_num
                inner_index += 1
                if inner_index == len(nums[outter_index]):
                    return [start, end]
                heapq.heappush(heap, (nums[outter_index][inner_index],
                                      outter_index, inner_index))
                max_num = max(max_num, nums[outter_index][inner_index])

