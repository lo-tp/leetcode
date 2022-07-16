from typing import List, Optional

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



def calculateRelevantPoints(v: int, h: int, sz: int):
    res = set()
    for i in range(0, sz):
        res.add((i, h))
        res.add((v, i))
    i, j = v - 1, h - 1
    while i > -1 and j > -1:
        res.add((i, j))
        i -= 1
        j -= 1
    i, j = v + 1, h + 1
    while i < sz and j < sz:
        res.add((i, j))
        i += 1
        j += 1
    i, j = v - 1, h + 1
    while i > -1 and j < sz:
        res.add((i, j))
        i -= 1
        j += 1
    i, j = v + 1, h - 1
    while i < sz and j > -1:
        res.add((i, j))
        i += 1
        j -= 1
    return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        h, path, taken, res = (
            0,
            [],
            [[0 for _ in range(0, n)] for _ in range(0, n)],
            [],
        )
        stack = [(i, False) for i in range(0, n)]
        while stack:
            v, flag = stack.pop()
            # print(v, h, flag)
            if flag:
                if len(path) == n:
                    t = [["Q" if i == j else "." for i in range(0, n)] for j in path]
                    res.append(["".join(i) for i in t])
                path.pop()
                h -= 1
                for (i, j) in calculateRelevantPoints(v, h, n):
                    taken[i][j] -= 1
            else:
                path.append(v)
                for (i, j) in calculateRelevantPoints(v, h, n):
                    taken[i][j] += 1
                h += 1
                stack.append((v, True))
                if h < n:
                    stack.extend([(i, False) for i in range(0, n) if not taken[i][h]])
            # print(v, h, flag)
            # for i in taken:
                # print(i)
        return res
