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

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        v_used=[0]*9
        h_used=[0]*9
        s_used=[0]*9
        for v in range(0,9):
            for h in range(0,9):
                if board[v][h]!='.':
                    bit_consumed=1<<(int(board[v][h]))
                    v_seen=v_used[v]
                    h_seen=h_used[h]
                    s_seen=s_used[(v//3)*3+(h//3)]
                    if (v_seen&bit_consumed) or (h_seen&bit_consumed) or (s_seen&bit_consumed):
                        return False
                    v_used[v]=v_seen|bit_consumed
                    h_used[h]=h_seen|bit_consumed
                    s_used[(v//3)*3+(h//3)]=s_seen|bit_consumed
        return True

