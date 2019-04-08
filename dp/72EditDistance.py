class Solution(object):
    def minDistanceTLE(self, word1, word2):
        s1, s2, sz1, sz2 = [[(-1, -1)]], [], len(word1), len(word2)
        while s1:
            for prevMatch in s1:
                (index1, index2) = prevMatch[-1]
                if index1 < sz1 and index2 < sz2:
                    for k in xrange(index1+1, sz1):
                        for w in xrange(index2+1, sz2):
                            if word1[k] == word2[w]:
                                s2.append(prevMatch+[(k, w)])
            if s2:
                s1, s2 = s2, []
            else:
                break
        res = sz1+sz2
        for match in s1:
            sum = 0
            for i in xrange(1, len(match)):
                sum += (max(match[i][0]-match[i-1][0],
                            match[i][1]-match[i-1][1])-1)
            sum += (max(sz1-match[-1][0], sz2-match[-1][1])-1)
            res = min(res, sum)
        return res
    def minDistance(self, word1, word2):
        sz1, sz2 = len(word1), len(word2)
        dp = [[0]*(sz2+1) for i in range(sz1+1)]
        for i in xrange(1, sz1+1):
            dp[i][0] = i
        for i in xrange(1, sz2+1):
            dp[0][i] = i
        for i in xrange(1, sz1+1):
            for k in xrange(1, sz2+1):
                if word1[i-1] == word2[k-1]:
                    dp[i][k] = dp[i-1][k-1]
                else:
                    dp[i][k] = min(dp[i-1][k-1], dp[i-1][k], dp[i][k-1])+1
        return dp[sz1][sz2]
