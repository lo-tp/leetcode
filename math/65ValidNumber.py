from re import match


class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        # integer
        if match(r'^[-+]?[\d]+$', s):
            return True
        # float
        if match(r'^[-+]?[\d]+\.[\d]+$', s):
            return True
        # -10e1 or 10e-1
        if match(r'^[-+]?[\d]+e-?[\d]+$', s):
            return True
        # 53.5e93
        if match(r'^[-+]?[\d]+\.[\d]+e[\d]+$', s):
            return True
    def isNumber(self, s):
        state, table = 0, [[0, 1, -1, 3, 2],
                           [8, 1, 5, -1, 4],
                           [-1, 9, -1, -1, -1],
                           [-1, 1, -1, -1, 2],
                           [8, 9, 5, -1, -1],
                           [-1, 6, -1, 7, -1],
                           [8, 6, -1, -1, -1],
                           [-1, 6, -1, -1, -1],
                           [8, -1, -1, -1, -1],
                           [8, 9, 5, -1, -1], ]
        for i in s:
            if i == ' ':
                state = table[state][0]
            elif i >= '0' and i <= '9':
                state = table[state][1]
            elif i == 'e':
                state = table[state][2]
            elif i == '+' or i == '-':
                state = table[state][3]
            elif i == '.':
                state = table[state][4]
            else:
                return False
            if state == -1:
                return False
        return state == 1 or state == 4 or state == 6 or state == 8 or state == 9

