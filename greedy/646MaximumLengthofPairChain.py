class Solution(object):
    def findLongestChainDP(self, pairs):
        pairs.sort()
        size = len(pairs)
        dp = [1]*size
        for i in xrange(0, size):
            for j in xrange(i, size):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)
    def findLongestChainTLE(self, pairs):
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

