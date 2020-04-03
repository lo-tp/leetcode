class Solution(object):
    def characterReplacement(self, original, k):
        s, res, sz, data = 0, 0, len(original), [0]*26
        max_count, ord_a = 0, ord('A')
        for f in xrange(0, sz):
            i = ord(original[f])-ord_a
            data[i] += 1
            max_count = max(max_count, data[i])
            if f-s+1-max_count > k:
                i = ord(original[s])-ord_a
                s += 1
                data[i] -= 1
            res = max(res, f-s+1)
        return res
    def characterReplacement(self, s, k):
        sz = len(s)
        if sz:
            sz = len(s)
            if k >= sz:
                return sz
            res = k
            data = [(s[0], 1, 1, k)]
            if sz > 1 and k:
                data = [(s[1], 1, 1, k-1)]
            while data:
                letter, length, index, mod_num = data.pop()
                if index == sz:
                    res = max(res, length)
                elif s[index] != letter:
                    res = max(res, length)
                    if mod_num:
                        data.append((letter, length+1, index+1, mod_num-1))
                    data.append((s[index], 1, index+1, k))
                else:
                    data.append((letter, length+1, index+1, mod_num))
            data.append((s[-1], 1, sz-2, k))
            if sz > 1 and k:
                data = [(s[-2], 1, 1, k-1)]
            while data:
                letter, length, index, mod_num = data.pop()
                if index == -1:
                    res = max(res, length)
                elif s[index] != letter:
                    res = max(res, length)
                    if mod_num:
                        data.append((letter, length+1, index-1, mod_num-1))
                    data.append((s[index], 1, index-1, k))
                else:
                    data.append((letter, length+1, index-1, mod_num))
            return res
        return 0

    def characterReplacement(self, original, k):
        s, res, sz, data = 0, 0, len(original), [0]*26
        max_count, ord_a = 0, ord('A')
        for f in xrange(0, sz):
            i = ord(original[f])-ord_a
            data[i] += 1
            max_count = max(max_count, data[i])
            if f-s+1-max_count > k:
                i = ord(original[s])-ord_a
                s += 1
                data[i] -= 1
            res = max(res, f-s+1)
        return res
