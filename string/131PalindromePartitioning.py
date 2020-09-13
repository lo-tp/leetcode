from collections import defaultdict


def isPalindrome(str):
    s, e = 0, len(str)-1
    while s <= e:
        if str[s] != str[e]:
            return False
        s += 1
        e -= 1
    return True


class Solution(object):
    def partition(self, str):
        data, sz = defaultdict(lambda: []), len(str)
        stack = [(0, sz-1, False)]
        while stack:
            s, e, flag = stack.pop()
            if flag:
                if (s, e) not in data:
                    tmp = set()
                    for i in xrange(s, e):
                        for j in data[(s, i)]:
                            for k in data[(i+1, e)]:
                                w = j[:]
                                w.extend(k)
                                # data[(s, e)].append(w)
                                tmp.add('*'.join(w))
                    data[(s, e)] = [i.split('*') for i in tmp]
                    t = str[s:e+1]
                    if isPalindrome(t):
                        data[(s, e)].append([t])
            else:
                stack.append((s, e, True))
                for i in xrange(s, e):
                    stack.append((s, i, False))
                    stack.append((i+1, e, False))
        return data[(0, sz-1)]
