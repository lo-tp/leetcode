class Prex():
    def __init__(self):
        self.children = [None]*26
        self.size = 0
        self.count = 0

    def add(self, word):
        tmp = self
        for w in word:
            index = ord(w)-97
            if tmp.size == 2:
                break
            if not tmp.children[index]:
                tmp.children[index] = Prex()
                tmp.size += 1
            tmp.count += 1
            tmp = tmp.children[index]


class Solution(object):
    def longestCommonPrefix(self, strs):
        size, prex = len(strs), Prex()
        for str in strs:
            prex.add(str)
        res = []
        while prex and prex.size == 1 and prex.count == size:
            index, prex = [(index, p)
                           for index, p in enumerate(prex.children) if p][0]
            res.append(index)
        return ''.join([chr(r+97) for r in res])
