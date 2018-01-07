class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0
        v = 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                v += 1
            elif moves[i] == 'D':
                v -= 1
            elif moves[i] == 'R':
                h += 1
            else:
                h -= 1
        return h == 0 and v == 0

soluction = Solution()
print soluction.judgeCircle('UD')
print soluction.judgeCircle('LL')
print soluction.judgeCircle('')
