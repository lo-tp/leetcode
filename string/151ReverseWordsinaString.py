from re import sub


class Solution(object):
    def reverseWords(self, s):
        return sub('(^ +| +$)', '', ' '.join(sub(' +', ' ', s).split(' ')[::-1]))
