class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits.reverse()
        if len(bits) is 1 or bits[1] is 0:
            return True
        else:
            iterator = (i for i in bits)
            n=1
            next(iterator)
            while 1:
                tem = next(iterator,None)
                if tem is 0 or tem is None:
                    break
                n+=1
            return n%2 is not 0

solution = Solution()
print solution.isOneBitCharacter([1, 0, 0])
print solution.isOneBitCharacter([1, 1, 1, 0])

