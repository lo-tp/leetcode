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
