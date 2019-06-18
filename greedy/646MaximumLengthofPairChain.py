class Solution(object):
    def findLongestChain(self, pairs):
        res, size = 0, len(pairs)
        stack = [[index] for index in xrange(0, size)]
        pairs.sort()
        while stack:
            path = stack.pop()
            res = max(len(path), res)
            end_index = size-res+1 if res else size
            for index in [index for index in xrange(path[-1]+1, end_index) if pairs[path[-1]][1] < pairs[index][0]]:
                new_path = path[:]
                new_path.append(index)
                stack.append(new_path)
        return res

