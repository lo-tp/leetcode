class Solution(object):
    def calculataPermulationNumber(self,n):
        return reduce(lambda x,y:x*y, range(1,n+1))
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        minNum=min(m,n)-1
        maxMun=max(m,n)-1
        return self.calculataPermulationNumber(maxMun+minNum)/self.calculataPermulationNumber(minNum)/self.calculataPermulationNumber(maxMun) if minNum else 1;
    def uniquePathsDp(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result=[[1 for i in xrange(m)] for j in xrange(n)]
        for verticalIndex in xrange(n):
            for horizontalIndex in xrange(m):
                if horizontalIndex and verticalIndex:
                    result[verticalIndex][horizontalIndex]=result[verticalIndex-1][horizontalIndex]+result[verticalIndex][horizontalIndex-1]
        return result[n-1][m-1]
s=Solution()
print s.uniquePaths(3,7)
