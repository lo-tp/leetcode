class Solution(object):
    def countBattleships(self, board):
        res, v_sz = 0, len(board)
        if v_sz:
            h_sz = len(board[0])
            if h_sz:
                if board[0][0] == 'X':
                    res += 1
                for v in xrange(1, v_sz):
                    if board[v][0] == 'X' and board[v-1][0] != 'X':
                        res += 1
                for h in xrange(1, h_sz):
                    if board[0][h] == 'X' and board[0][h-1] != 'X':
                        res += 1
                for v in xrange(1, v_sz):
                    for h in xrange(1, h_sz):
                        if board[v][h] == 'X' and board[v-1][h] != 'X' and board[v][h-1] != 'X':
                            res += 1
        return res
