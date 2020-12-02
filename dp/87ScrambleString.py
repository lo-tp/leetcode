from collections import defaultdict


class Solution(object):
    def isScramble(self, s1, s2):
        data = defaultdict(set)
        stack = [(s1, False)]
        while stack:
            string, flag = stack.pop()
            if flag:
                sz = len(string)
                for i in range(1, sz):
                    for x in data[string[:i]]:
                        for y in data[string[i:]]:
                            data[string].add(x+y)
                            data[string].add(y+x)
            elif not data[string]:
                sz = len(string)
                if sz == 1:
                    data[string].add(string)
                else:
                    stack.append((string, True))
                    for i in range(1, sz):
                        stack.append((string[:i], False))
                        stack.append((string[i:], False))
        return s2 in data[s1]

