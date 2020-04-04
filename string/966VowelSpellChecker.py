vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
ord_a = ord('A')

class Trie():
    def __init__(self):
        self.data = [None]*58
        self.val = None
        self.word = None

    def add(self, s, index):
        tmp = self
        for i in [ord(j)-ord_a for j in s]:
            if not tmp.data[i]:
                tmp.data[i] = Trie()
            tmp = tmp.data[i]
        tmp.val = index
        tmp.word = s

    def find(self, s):
        sz, res = len(s), []
        for i in [0, 1, 2]:
            if res:
                break
            stack = [(0, self)]
            while stack:
                t, tm = stack.pop()
                if t == sz and tm.val != None:
                    res.append((tm.val, tm.word))
                elif t != sz:
                    if not i:
                        j = ord(s[t])-ord_a
                        if tm.data[j]:
                            stack.append((t+1, tm.data[j]))
                    elif i == 1:
                        for j in [
                                ord(tmp)-ord_a for tmp in [s[t].upper(), s[t].lower()]]:
                            if tm.data[j]:
                                stack.append((t+1, tm.data[j]))
                    else:
                        if s[t] in vowels:
                            for j in [ord(tmp)-ord_a for tmp in vowels]:
                                if tm.data[j]:
                                    stack.append((t+1, tm.data[j]))
                        else:
                            for j in [
                                    ord(tmp)-ord_a for tmp in [s[t].upper(), s[t].lower()]]:
                                if tm.data[j]:
                                    stack.append((t+1, tm.data[j]))
        return res
class Solution(object):
    def spellchecker(self, wordlist, queries):
        res, trie = ['' for i in queries], Trie()
        for i, w in enumerate(wordlist):
            trie.add(w, i)

        for i, w in enumerate(queries):
            t = trie.find(w)
            if t:
                t.sort()
                res[i] = t[0][1]
        return res
