from sys import maxint
from collections import Counter


class Solution(object):
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
