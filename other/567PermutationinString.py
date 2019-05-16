from collections import Counter


class Solution(object):
    def checkInclusion(self, target, str):
        start, target_size, str_size = 0, len(
            target), len(str)
        if str_size >= target_size:
            last_start = str_size-target_size
            while start <= last_start:
                end = start
                data = Counter(target)
                remaining_num = len(data.keys())
                while end < str_size and str[end] in data:
                    if data[str[end]]:
                        data[str[end]] -= 1
                        if not data[str[end]]:
                            remaining_num -= 1
                            if not remaining_num:
                                return True
                    else:
                        while str[start] != str[end]:
                            if not data[str[start]]:
                                remaining_num += 1
                            data[str[start]] += 1
                            start += 1
                        start += 1
                    end += 1
                start = end+1
        return False

