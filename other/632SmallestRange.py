from sys import maxint


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
