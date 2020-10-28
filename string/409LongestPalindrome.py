from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        res, data, flag = 0, Counter(s), True
        for i in sorted(data.values())[::-1]:
            if i % 2:
                res += i if flag else i-1
                flag = False
            else:
                res += i
        return res
