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

