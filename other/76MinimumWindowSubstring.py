from sys import maxint
from collections import Counter

class Solution(object):
    def minWindowBetter(self, s, t):
        slow, sz_s, sz_t, data = 0, len(s), len(t), Counter(t)
        res, min_length = '', maxint
        for fast in xrange(0, sz_s):
            if s[fast] in data:
                if data[s[fast]] > 0:
                    sz_t -= 1
                data[s[fast]] -= 1
            if not sz_t:
                while s[slow] not in data or data[s[slow]]:
                    if s[slow] in data:
                        data[s[slow]] += 1
                    slow += 1
                sz_t += 1
                data[s[slow]] += 1
                te = fast-slow+2
                if te < min_length:
                    min_length = te
                    res = s[slow: fast+1]
                slow += 1
        return res
    def minWindowEasyToUnderstand(self, source, target):
        res, source_size, target_size = '', len(source), len(target)
        if source_size >= target_size:
            head, tail, start, end, data = 0, maxint, 0, 0, Counter(target)
            data_size, found_size, found = len(
                data.keys()), 0, defaultdict(lambda: 0)
            while end < source_size:
                char = source[end]
                if char in data:
                    found[char] += 1
                    if found[char] == data[char]:
                        found_size += 1
                        if found_size == data_size:
                            while found_size == data_size:
                                while source[start] not in data:
                                    start += 1
                                if found[source[start]] == data[source[start]]:
                                    found_size -= 1
                                found[source[start]] -= 1
                                start += 1
                            if end-start+1 < tail-head:
                                tail, head = end, start-1
                end += 1
            if tail != maxint:
                res = source[head:tail+1]
        return res
    def minWindowBest(self, source, target):
        head, tail, source_size, target_size = 0, maxint, len(
            source), len(target)
        if source_size >= target_size:
            left, right,  data = 0,  0, Counter(
                target),
            remaining_num = len(data.keys())
            while True:
                while remaining_num and right < source_size:
                    char = source[right]
                    if char in data:
                        data[char] -= 1
                        if not data[char]:
                            remaining_num -= 1
                    right += 1
                if remaining_num:
                    break
                while not remaining_num and left < right:
                    char = source[left]
                    if char in data:
                        if not data[char]:
                            remaining_num += 1
                        data[char] += 1
                    left += 1
                if right-left+1 < tail-head:
                    head, tail = left-1, right
        return '' if tail == maxint else source[head:tail]

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
    def minWindow(self, s, t):
        sz_s, count = len(s), Counter(t)
        sz_t, l, res, res_min = len(count.keys()), 0, '', maxsize
        for r in range(0, sz_s):
            if s[r] in count:
                count[s[r]] -= 1
                if not count[s[r]]:
                    sz_t -= 1
                if not sz_t:
                    while True:
                        if s[l] in count:
                            if count[s[l]] == 0:
                                break
                            count[s[l]] += 1
                        l += 1
                    sz_t += 1
                    te = r-l+1
                    if te < res_min:
                        res_min, res = te, s[l:r+1]
                    count[s[l]] += 1
                    l += 1
        return res
