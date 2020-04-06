class Solution(object):
    def possibleBipartition(self, N, dislikes):
        data = [set() for i in xrange(0, N+1)]
        t = [set(), set()]
        for i, j in dislikes:
            data[i].add(j)
            data[j].add(i)
        for i, j in enumerate(data):
            if j:
                stack, te = [i], True
                while stack:
                    tmp = []
                    for k in stack:
                        if k in (t[1] if te else t[0]):
                            return False
                        (t[0] if te else t[1]).add(k)
                        for w in data[k]:
                            tmp.append(w)
                        data[k] = []
                    stack = tmp
                    te = not te
        return True
