from collections import Counter


class Solution(object):
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

