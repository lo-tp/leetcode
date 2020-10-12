class Solution(object):
    def getPermutation(self, n, k):
        seen, options, i, data = set(),   [
            j for j in xrange(n, 0, -1)], 0, []
        stack = [(j, False) for j in options]
        while True:
            num, flag = stack.pop()
            if flag:
                if len(data) == n:
                    i += 1
                    if i == k:
                        return ''.join([j for j in data])
                seen.remove(num)
                data.pop()
            else:
                seen.add(num)
                data.append(str(num))
                stack.append((num, True))
                stack.extend([(j, False) for j in options if j not in seen])


