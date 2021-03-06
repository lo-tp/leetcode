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

    def partition(self, str):
        stack, data = [(str, False)], {}
        while stack:
            s, flag = stack.pop()
            if s not in data:
                if flag:
                    data[s] = []
                    for i in xrange(1, len(s)+1):
                        prefix, surfix = s[:i], s[i:]
                        if prefix == prefix[::-1]:
                            for i in data[surfix]:
                                data[s].append([prefix]+i)
                            if not surfix:
                                data[s].append([prefix])
                else:
                    stack.append((s, True))
                    for i in xrange(1, len(s)+1):
                        p = s[:i]
                        if p == p[::-1]:
                            stack.append((s[i:], False))
        return data[str]

    def partition(self, s):
        data, stack = {}, [(s, False)]
        while stack:
            str, flag = stack.pop()
            if flag:
                data[str] = []
                for i in xrange(1, len(str)):
                    prefix, surfix = str[:i], str[i:]
                    if prefix == prefix[::-1]:
                        for j in data[surfix]:
                            data[str].append([prefix]+j)
                if str == str[::-1]:
                    data[str].append([str])
            else:
                stack.append((str, True))
                for i in xrange(1, len(str)):
                    prefix, surfix = str[:i], str[i:]
                    if prefix == prefix[::-1] and surfix not in data:
                        stack.append((surfix, False))
        return data[s]
    def partition(self, s):
        data, sz = [[] for _ in s], len(s)
        stack = [(i, False) for i in xrange(0, sz)]
        while stack:
            index, flag = stack.pop()
            if flag:
                for i in xrange(index+1, sz):
                    prefix = s[index:i]
                    if prefix == prefix[::-1]:
                        for j in data[i]:
                            t = [prefix]
                            t.extend(j)
                            data[index].append(t)
                prefix = s[index:]
                if prefix == prefix[::-1]:
                    data[index].append([prefix])
            else:
                if not data[index]:
                    stack.append((index, True))
                    for i in xrange(index+1, sz-1):
                        prefix = s[index:i]
                        if prefix == prefix[::-1]:
                            stack.append((i, False))
        return data[0]

    def partition(self, s):
        stack, sz, data = [(0, False)], len(s), [None for _ in s]
        while stack:
            index, visited = stack.pop()
            if visited:
                for m in range(index+1, sz):
                    l = s[index:m]
                    if isPalindrome(l):
                        for t in data[m]:
                            te = [l]
                            te.extend(t)
                            data[index].append(te)
                t = s[index:]
                if isPalindrome(t):
                    data[index].append([t])
            elif data[index] == None:
                stack.append((index, True))
                data[index] = []
                for m in range(index+1, sz):
                    l = s[index:m]
                    if isPalindrome(l):
                        stack.append((m, False))
        return data[0]

