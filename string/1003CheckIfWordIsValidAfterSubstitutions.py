class Solution(object):
    def isValid(self, S):
        data = [0]*2
        for index, i in enumerate(S):
            if i == 'a':
                data[0] += 1
            elif i == 'b':
                if not data[0] or (index and S[index-1] == 'b'):
                    return False
                data[0] -= 1
                data[1] += 1
            else:
                if not data[1] or S[index-1] == 'a':
                    return False
                data[1] -= 1
        return not data[0] and not data[1]

