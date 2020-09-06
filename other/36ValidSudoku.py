class Solution(object):
    def isValidSudoku(self, board):
        v_data, h_data, c_data = [set() for _ in xrange(0, 9)], [set() for _ in xrange(
            0, 9)], [[set() for _ in xrange(0, 3)] for _ in xrange(0, 3)]

        def getSet(v, h):
            return (v_data[v], h_data[h], c_data[v/3][h/3])

        for v in xrange(0, 9):
            for h in xrange(0, 9):
                t = board[v][h]
                if t != '.':
                    v_set,  h_set, c_set = getSet(v, h)
                    if t in v_set or t in h_set or t in c_set:
                        return False
                    v_set.add(t)
                    c_set.add(t)
                    h_set.add(t)
        return True
