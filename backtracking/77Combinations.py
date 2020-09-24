class Solution(object):
    def combine(self, n, k):
        res = []
        if k and k < n:
            stack = [([], 0, K)]
            while stack:
                path, index, remaining = stack.pop()
                if not remaining:
                    res.append(path)
                else:
                    remaining -= 1
                    for i in xrange(index, n-remaining+1):
                        new_path = path[:]
                        new_path.append(i)
                        stack.append((new_path, i+1, remaining))
        return res

    def combine(self, n, k):
        res, current, stack, options = [], [], [
            (i, False) for i in xrange(1, n+1)], set()

        while stack:
            option, visited = stack.pop()
            if visited:
                current.pop()
            else:
                stack.append((option, True))
                current.append(option)
                if len(current) == k:
                    res.append(current[:])
                else:
                    stack.extend([(i, False) for i in xrange(option+1, n+1)])
        return res
