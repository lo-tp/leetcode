class Prie():
    def __init__(self):
        self.data = [None for _ in xrange(0, 26)]

    def add(self, str, start_index):
        flag, res, tmp = True, 0, self.data
        for i in xrange(start_index, len(str)):
            index = ord(str[i])-97
            if not tmp[index]:
                tmp[index] = Prie()
                flag = False
            if flag:
                res += 1
            tmp = tmp[index].data
        return res


class Solution(object):
    def longestDupSubstring(self, S):
        prie, res = Prie(), ''
        for i in xrange(0, len(S)):
            tmp = prie.add(S, i)
            if len(res) < tmp:
                res = S[i:i+tmp]
        return res

