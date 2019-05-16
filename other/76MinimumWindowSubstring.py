from sys import maxint
from collections import Counter


class Solution(object):
    def minWindowBetter(self, source, target):
        source_size, target_size, start, end, start_index, end_index = len(
            source), len(target), 0, 0, 0, maxint
        if target_size and target_size <= source_size:
            data = Counter(target)
            remaining_num = len(data.keys())
            while True:
                while remaining_num and end < source_size:
                    if source[end] in data:
                        data[source[end]] -= 1
                        if not data[source[end]]:
                            remaining_num -= 1
                    end += 1
                if remaining_num:
                    break
                else:
                    while not remaining_num and start < end:
                        if end-start < end_index-start_index:
                            end_index, start_index = end, start
                        if source[start] in data:
                            if not data[source[start]]:
                                remaining_num += 1
                            data[source[start]] += 1
                        start += 1
        return '' if maxint == end_index else source[start_index:end_index]
    def minWindow(self, str, target):
        res, start,  end, data, left_index, right_index, size = '', 0, maxint, Counter(
            target), 0, 0, len(str)
        remaining_num = len(data.keys())
        if str and target:
            while True:
                if remaining_num and right_index < size:
                    char = str[right_index]
                    if char in data:
                        data[char] -= 1
                        if data[char] == 0:
                            remaining_num -= 1
                    right_index += 1
                else:
                    while left_index < right_index and remaining_num == 0:
                        if right_index-left_index < end-start:
                            start, end = left_index, right_index
                        char = str[left_index]
                        if char in data:
                            if data[char] == 0:
                                remaining_num += 1
                            data[char] += 1
                        left_index += 1
                    if right_index == size:
                        break
            if end-start <= size:
                res = str[start:end]
        return res
