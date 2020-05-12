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

    def numMovesStonesBetter(self, a, b, c):
        data = [a, b, c]
        data.sort()
        if data[-1]-data[0] == 3:
            return [1, 1]
        elif data[-1]-data[0] == 2:
            return [0, 0]
        else:
            return [2, data[-1]-data[0]-2]

    def numMovesStones(self, a, b, c):
        a, b, c = sorted([a, b, c])
        mini = 2
        if a+1 == b and b+1 == c:
            mini = 0
        elif a >= b-2 or b >= c-2:
            mini = 1
        return [mini, c-a-2]
