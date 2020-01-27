def getInt(s):
    return 0 if s == 'E' else ord(s)-ord('0')


class Solution(object):
    def pathsWithMaxScore(self, board):
        mod, v_sz, h_sz = 10**9+7, len(board), len(board[0])
        low, high = [[-1, 0] for i in board[0]], [[-1, 0] for i in board[0]]
        low[-1] = [0, 1]
        for i in xrange(h_sz-2, -1, -1):
            if board[-1][i] != 'X':
                low[i] = [getInt(board[-1][i])+low[i+1][0], 1]
            else:
                break

        for v in xrange(v_sz-2, -1, -1):
            if board[v][-1] != 'X' and low[-1][0] != -1:
                high[-1] = [getInt(board[v][-1])+low[-1][0], low[-1][1]]
            else:
                high[-1][0] = -1
            for h in xrange(h_sz-2, -1, -1):
                high[h][0] = -1
                if board[v][h] != 'X':
                    j, k = -1, -1
                    if high[h+1][0] > j:
                        j, k = high[h+1]
                    elif high[h+1][0] == j:
                        k += high[h+1][1]
                    if low[h][0] > j:
                        j, k = low[h]
                    elif low[h][0] == j:
                        k += low[h][1]
                    if low[h+1][0] > j:
                        j, k = low[h+1]
                    elif low[h+1][0] == j:
                        k += low[h+1][1]
                    if j > -1:
                        high[h] = [j+getInt(board[v][h]), k]
            high, low = low, high
        return [i % mod for i in low[0]] if low[0][0] > -1 else [0, 0]

