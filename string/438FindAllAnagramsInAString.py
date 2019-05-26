from collections import Counter


class Solution(object):
    def findAnagramsRight(self, s, p):
        start, end, res, data, size = 0, 0, [], Counter(p), len(s)
        first_pos, remaining_num, found_num, found_data = {}, len(
            data.keys()), 0, data.copy()
        while end < size:
            char = s[end]
            if char not in data:
                end += 1
                start = end
                first_pos, found_num, found_data = {}, 0, data.copy()
            elif not found_data[char]:
                start = end = first_pos[char] + \
                    1 if char in first_pos else start+1
                first_pos, found_num, found_data = {}, 0, data.copy()
            else:
                if found_data[char] == data[char]:
                    first_pos[char] = end
                found_data[char] -= 1
                if not found_data[char]:
                    found_num += 1
                    if found_num == remaining_num:
                        res.append(start)
                        found_data[s[start]] += 1
                        first_pos.pop(s[start], None)
                        start += 1
                        found_num -= 1
                end += 1
        return res
    // test case below can prove this solution wrong
    // "aabaaaaa", "aab"

    def findAnagramsBetter(self, s, p):
        start, end, size, res, data, first_position = 0, 0, len(
            s), [], Counter(p), {}
        remaining_num, found_num, to_find_data = len(
            data.keys()), 0, data.copy()
        while end < size:
            char = s[end]
            if char in data:
                if not to_find_data[char]:
                    start = end = first_position[char]+1
                    first_position, found_num, to_find_data = {}, 0, data.copy()
                else:
                    if data[char] == to_find_data[char]:
                        first_position[char] = end
                    to_find_data[char] -= 1
                    if not to_find_data[char]:
                        found_num += 1
                        if found_num == remaining_num:
                            res.append(start)
                            to_find_data[s[start]] += 1
                            found_num -= 1
                            start += 1
                    end += 1
            else:
                end += 1
                start, first_position, found_num, to_find_data = end, {}, 0, data.copy()
        return res

    def findAnagrams(self, s, p):
        size, last_start, res, start, data = len(
            s), len(s)-len(p), [], 0, Counter(p)
        remaining_num = len(data.keys())
        end, tmp, match, match_num = 0, {}, data.copy(), remaining_num
        while start <= last_start:
            while end < size and match_num and s[end] in match and match[s[end]] > 0:
                match[s[end]] -= 1
                if not match[s[end]]:
                    match_num -= 1
                tmp[s[end]] = end
                end += 1
            if end == size:
                break
            elif not match_num:
                res.append(start)
                match[s[start]] += 1
                match_num += 1
                start += 1
            elif s[end] not in match:
                match_num = remaining_num
                match = data.copy()
                start = end+1
                end = start
            else:
                match_num = remaining_num
                match = data.copy()
                start = tmp[s[end]]+1
                end = start
        if not match_num:
            res.append(start)
        return res
