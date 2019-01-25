class Solution(object):
    def lengthOfLongestSubstringBruteForce(self, s):
        sz = len(s)
        lastIndex = sz-1
        res, index = 0, 0
        while index <= lastIndex:
            key = {}
            i = index
            while i < sz and s[i] not in key:
                key[s[i]] = 1
                i += 1
            res = max(res, i-index)
            index += 1
            lastIndex = sz-res
        return res
    def lengthOfLongestSubstring(self, s):
        res, sz, firstIndex = 0, len(s), 0
        firstLimit = sz
        while firstIndex < firstLimit:
            i = firstIndex
            data = {}
            while i < sz and s[i] not in data:
                data[s[i]] = i
                i += 1
            res = max(res, i-firstIndex)
            firstLimit = sz-res
            if i < sz:
                firstIndex = data[s[i]]+1
        return res
