from collections import defaultdict


class Solution(object):
    def diffWaysToCompute(self, input):
        total, data = 0, []
        ord_0, ord_9 = ord('0'), ord('9')
        seen = defaultdict(list)
        for i in input:
            t = ord(i)
            if t < ord_0 or t > ord_9:
                data.append(total)
                data.append(i)
                total = 0
            else:
                total = total*10+t-ord_0
        data.append(total)
        sz = len(data)
        stack = [(0, sz, False)]
        while stack:
            l, r, flag = stack.pop()
            if not flag:
                if not seen[(l, r)]:
                    if l+1 == r:
                        seen[(l, r)].append(data[l])
                    else:
                        stack.append((l, r, True))
                        for i in range(l, r):
                            if data[i] == '+' or data[i] == '-' or data[i] == '*':
                                stack.append((l, i, False))
                                stack.append((i+1, r, False))
            else:
                for i in range(l, r):
                    if data[i] == '+':
                        for j in seen[(l, i)]:
                            for w in seen[(i+1, r)]:
                                seen[(l, r)].append(j+w)
                    elif data[i] == '*':
                        for j in seen[(l, i)]:
                            for w in seen[(i+1, r)]:
                                seen[(l, r)].append(j*w)
                    elif data[i] == '-':
                        for j in seen[(l, i)]:
                            for w in seen[(i+1, r)]:
                                seen[(l, r)].append(j-w)
        return seen[(0, sz)]

