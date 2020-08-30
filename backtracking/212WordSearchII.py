class Solution(object):
    def findWords(self, board, words):
        res, v_sz = [], len(board)
        if v_sz:
            h_sz = len(board[0])
            for w in words:
                signal, t, sz = False, 0, len(w)
                print board, w
                for v in xrange(0, v_sz):
                    if signal:
                        break
                    for h in xrange(0, h_sz):
                        stack = [(v, h, False)]
                        while stack:
                            i, j, flag = stack.pop()
                            if i < 0 or i >= v_sz or j < 0 or j >= h_sz:
                                continue
                            if flag:
                                t -= 1
                                board[i][j] = w[t]
                            elif board[i][j] == w[t]:
                                t += 1
                                board[i][j] = ' '
                                stack.append((i, j, True))
                                if t == sz:
                                    res.append(w)
                                    signal = True
                                    while stack:
                                        i, j, flag = stack.pop()
                                        if flag:
                                            t -= 1
                                            board[i][j] = w[t]
                                    break
                                stack.extend([(k, m, False) for k, m in [
                                             (i+1, j), (i-1, j), (i, j+1), (i, j-1)]])
                        if signal:
                            break

        return res
