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
    def solveSudoku(self, board):
        v_data, h_data, c_data = [set() for _ in xrange(0, 9)], [set() for _ in xrange(
            0, 9)], [[set() for _ in xrange(0, 3)] for _ in xrange(0, 3)]

        def getSet(v, h):
            return (v_data[v], h_data[h], c_data[v/3][h/3])

        for v in xrange(0, 9):
            for h in xrange(0, 9):
                if board[v][h] != '.':
                    v_set,  h_set, c_set = getSet(v, h)
                    v_set.add(board[v][h])
                    c_set.add(board[v][h])
                    h_set.add(board[v][h])
                    board[v][h] += ' '

        stack = [(0, 0, 0)]
        while stack:
            v, h, t = stack.pop()
            if v == 9:
                break
            v_set, h_set, c_set = getSet(v, h)
            if t > 0:
                te = '{}'.format(t)
                v_set.remove(te)
                h_set.remove(te)
                c_set.remove(te)
            else:
                t = abs(t)
            next_v, next_h = (v+1, 0) if h == 8 else (v, h+1)
            if len(board[v][h]) < 2 and t < 9:
                t += 1
                te = '{}'.format(t)
                if te in v_set or te in h_set or te in c_set:
                    stack.append((v, h, -t))
                    continue
                stack.append((v, h, t))
                v_set.add(te)
                h_set.add(te)
                c_set.add(te)
                stack.append((next_v, next_h, 0))
                board[v][h] = te
            elif len(board[v][h]) == 2:
                stack.append((next_v, next_h, 0))

        for v in xrange(0, 9):
            for h in xrange(0, 9):
                board[v][h] = board[v][h].strip()
