class Solution(object):
    def numMovesStones(self, a, b, c):
        data = [a, b, c]
        data.sort()
        a, b, c = data
        if b-a == 1 and c-b == 1:
            return [0, 0]
        elif b-a == 1:
            return [1, c-b-1]
        elif c-b == 1:
            return [1, b-a-1]
        elif b-a == 2:
            return [1, c-a-2]
        elif c-b == 2:
            return [1, c-a-2]
        else:
            return [2, c-a-2]
