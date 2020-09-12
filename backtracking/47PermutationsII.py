class Solution(object):
    def permuteUnique(self, n):
        res, sz, seen, stack, data = list(), len(n),  set(
        ), [(i, False) for i in xrange(0, len(n))], []
        str_seen = set()
        while stack:
            index, flag = stack.pop()
            if index == sz:
                continue
            if flag:
                seen.remove(index)
                data.pop()
                continue
            data.append(n[index])
            if len(data) == sz:
                    res.append(data[:])
            seen.add(index)
            stack.append((index, True))
            stack.extend([(i, False)
                          for i in xrange(0, sz) if i not in seen])
        return res
    def permuteUnique(self, n):
        sz, t, res, seen, seen_str = len(n), [], [], set(), set()
        stack = [(i, False) for i in xrange(0, sz)]
        while stack:
            index, flag = stack.pop()
            if flag:
                t.pop()
                seen.remove(index)
            else:
                t.append('{}'.format(n[index]))
                stack.append((index, True))
                seen.add(index)
                m = ''.join(t)
                if m not in seen_str:
                    seen_str.add(m)
                    if len(t) == sz:
                        res.append([int(i) for i in t])
                    else:
                        stack.extend([(i, False)
                                      for i in xrange(0, sz) if i not in seen])
        return res
