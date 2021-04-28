from collections import Counter
from copy import deepcopy


class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        res, data, sz = [], Counter(words), len(s)
        word_sz, words_sz = len(words[0]), len(words)
        intervals = [i*word_sz for i in range(0, words_sz)]
        for start in range(0, sz-word_sz*words_sz+1):
            t = 0
            tem = deepcopy(data)
            for interval in intervals:
                te = start+interval
                w = s[te:te+word_sz]
                if w not in tem or not tem[w]:
                    break
                tem[w] -= 1
                t += 1
            if t == words_sz:
                res.append(start)
        return res
