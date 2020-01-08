class Solution(object):
    def slidingPuzzle(self, board):
        original = ''.join([str(i) for i in board[0]]) + \
            ''.join([str(i) for i in board[1]])
        index = original.index('0')
        data, next_index = set(), [[3, 1], [0, 4, 2], [1, 5], [
            0, 4], [3, 1, 5], [2, 4]]
        stack, step = [(original, index)], 0
        while stack:
            tem = []
            while stack:
                s, i = stack.pop()
                for n in next_index[i]:
                    t = list(s)
                    t[i], t[n] = t[n], t[i]
                    t = ''.join(t)
                    if s == '123450':
                        return step
                    elif t not in data:
                        tem.append((t, n))
                        data.add(s)
            stack = tem
            step += 1
        return -1

