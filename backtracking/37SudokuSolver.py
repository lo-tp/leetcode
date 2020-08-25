def getCoordinates(v, h):
    return [v, h, (v/3, h/3)]

class Solution(object):
    def solveSudoku(self, board):
        def dfs(v, h):
            if v == 9:
                return True
            next_v, next_h = (v+1, 0) if h == 8 else (v, h+1)
            if len(board[v][h]) > 1:
                return dfs(next_v, next_h)
            for i in [str(i) for i in xrange(1, 10)]:
                v_index, h_index, c_index = getCoordinates(v, h)
                v_set, h_set, c_set = v_data[v_index], h_data[h_index], c_data[c_index[0]][c_index[1]]
                if i in v_set or i in h_set or i in c_set:
                    continue
                v_set.add(i)
                h_set.add(i)
                c_set.add(i)
                board[v][h] = i
                if dfs(next_v, next_h):
                    return True
                v_set.remove(i)
                h_set.remove(i)
                c_set.remove(i)
            return False
        v_data, h_data, c_data = [set() for _ in xrange(0, 9)], [set() for _ in xrange(
            0, 9)], [[set() for _ in xrange(0, 3)] for _ in xrange(0, 3)]

        for v in xrange(0, 9):
            for h in xrange(0, 9):
                if board[v][h] != '.':
                    v_index, h_index, c_index = getCoordinates(v, h)
                    v_data[v_index].add(board[v][h])
                    h_data[h_index].add(board[v][h])
                    c_data[c_index[0]][c_index[1]].add(board[v][h])
                    board[v][h] += ' '
        dfs(0, 0)
        for v in xrange(0, 9):
            for h in xrange(0, 9):
                board[v][h] = board[v][h].strip()
