class Solution(object):
    def isAlienSorted(self, words, order):
        data = {}
        for i, j in enumerate(order):
            data[j] = i
        for i in xrange(0, len(words)-1):
            flag, t, te = False, words[i], words[i+1]
            for tem in xrange(0, min(len(t), len(te))):
                if data[t[tem]] > data[te[tem]]:
                    return False
                elif data[t[tem]] < data[te[tem]]:
                    flag = True
                    break
            if not flag and len(t) > len(te):
                return False
        return True
