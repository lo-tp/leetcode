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
    def findWords(self, board, words):
        res, v_sz = [], len(board)
        if v_sz:
            h_sz = len(board[0])
            if h_sz:
                trie = {}
                for w in words:
                    t = trie
                    for m in w:
                        t = t.setdefault(m, {})
                    t['-'] = w
                for i in xrange(0, v_sz):
                    for j in xrange(0, h_sz):
                        if board[i][j] in trie:
                            stack = [(i, j, trie, False, board[i][j])]
                            while stack:
                                v, h, node, flag, val = stack.pop()
                                if flag:
                                    board[v][h] = val
                                    continue
                                stack.append((v, h, node, True, val))
                                node = node[val]
                                t = node.pop('-', False)
                                if t:
                                    res.append(t)
                                stack.extend([(w, m, node, False, board[w][m]) for w, m in [
                                             (v+1, h), (v-1, h), (v, h+1), (v, h-1)] if w >= 0 and w < v_sz and m >= 0 and m < h_sz and board[w][m] in node])
                                board[v][h] = '*'
        return res
