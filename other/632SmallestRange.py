from sys import maxint


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
