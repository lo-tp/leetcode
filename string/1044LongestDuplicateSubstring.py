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
    def longestDupSubstringTLE(self, S):
        prie, res = Prie(), ''
        for i in xrange(0, len(S)):
            tmp = prie.add(S, i)
            if len(res) < tmp:
                res = S[i:i+tmp]
        return res
    def longestDupSubstringMLE(self, S):
        res, l, r, a_num = '', 0, len(S)-1, ord('a')
        while l <= r:
            tmp, id, existence, size = None, 0, set(), l+(r-l)/2
            tem = 26**(size-1)
            for i in xrange(0, size):
                id = id*26+ord(S[i])-a_num
            existence.add(id)
            for i in xrange(size, len(S)):
                tail, prev_head = S[i], S[i-size]
                id = (id - (ord(prev_head)-a_num)*tem)*26+ord(tail)-a_num
                if id in existence:
                    tmp = S[i-size+1:i+1]
                    break
                existence.add(id)
            if tmp:
                l = size+1
                res = tmp
            else:
                r = size-1
        return res

