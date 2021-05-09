class Solution(object):
    def restoreIpAddresses(self, s):
        data, sz, current, res = [], len(s), [], set()
        if sz > 3 and sz < 13:
            stack = [(i, 0, False) for i in range(0, sz-3)]
            for i in range(0, sz):
                data.append([])
                if s[i] == '0':
                    data[-1].append('0')
                else:
                    for j in range(1, 4):
                        m = s[i:j+i]
                        if int(m) < 256:
                            data[-1].append(m)
            while stack:
                index, inner_index, visited = stack.pop()
                if visited:
                    if len(current) == 4:
                        t = '.'.join(current)
                        if len(t) == sz+3:
                            res.add(t)
                    current.pop()
                    inner_index += 1
                    if inner_index < len(data[index]):
                        stack.append((index, inner_index, False))
                else:
                    stack.append((index, inner_index, True))
                    current.append(data[index][inner_index])
                    m = index+len(current[-1])
                    if len(current) < 4 and m < sz and data[m]:
                        stack.append((m, 0, False))
        return list(res)
