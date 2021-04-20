class Solution(object):
    def solveNQueens(self, sz):
        t, res, remain = [], [], [
            [0 for _ in xrange(0, sz)] for _ in xrange(0, sz)]
        index, stack, affect, board = 0, [(i, False)
                                          for i in xrange(0, sz)], [[[] for _ in xrange(0, sz)] for _ in xrange(0, sz)], ['.']*sz
        for i in xrange(0, sz-1):
            for j in xrange(0, sz):
                for w in xrange(i+1, sz):
                    affect[i][j].append((w, j))
                for w in xrange(1, sz-max(i, j)):
                    affect[i][j].append((i+w, j+w))
                for w in xrange(1, min(j+1, sz-i)):
                    affect[i][j].append((i+w, j-w))

        while stack:
            val, flag = stack.pop()
            if flag:
                index -= 1
                t.pop()
                for i, j in affect[index][val]:
                    remain[i][j] -= 1
            else:
                t.append(val)
                stack.append((val, True))
                for i, j in affect[index][val]:
                    remain[i][j] += 1
                index += 1
                if index == sz:
                    te = []
                    for i in t:
                        board[i] = 'Q'
                        te.append(''.join(board))
                        board[i] = '.'
                    res.append(te)
                else:
                    stack.extend([(i, False)
                                  for i in xrange(0, sz) if not remain[index][i]])
        return res
