class Solution(object):
    def solve(self, board):
        column_size = len(board)
        if column_size:
            stack, data, row_size = [], {}, len(board[0])
            tmp = row_size-1
            for i in xrange(0, column_size):
                stack.append((i, 0))
                stack.append((i, tmp))
            tmp = column_size-1
            for i in xrange(0, row_size):
                stack.append((0, i))
                stack.append((tmp, i))
            while stack:
                column_index, row_index = stack.pop()
                hash = '{} {}'.format(column_index, row_index)
                if row_index >= 0 and row_index < row_size and column_index >= 0 and column_index < column_size and hash not in data:
                    data[hash] = board[column_index][row_index] == 'O'
                    if data[hash]:
                        stack.append((column_index-1, row_index))
                        stack.append((column_index, row_index-1))
                        stack.append((column_index+1, row_index))
                        stack.append((column_index, row_index+1))

            for row_index in xrange(1, row_size-1):
                for column_index in xrange(1, column_size-1):
                    hash = '{} {}'.format(column_index, row_index)
                    if hash not in data or not data[hash]:
                        board[column_index][row_index] = 'X'


    def solve(self, board: List[List[str]]) -> None:
        v_sz, h_sz=len(board), len(board[0])

        def mark(v, h):
            stack=[(v,h)]
            while stack:
                v_idx, h_idx=stack.pop()
                if v_idx >= 0 and v_idx < v_sz and h_idx >= 0 and h_idx < h_sz:
                    if board[v_idx][h_idx]=='O':
                        board[v_idx][h_idx]='o'
                        stack.extend([(v_idx,h_idx-1), (v_idx, h_idx+1), (v_idx-1, h_idx), (v_idx+1, h_idx)])

        for h_idx in range(0, h_sz):
            mark(0,h_idx)
            mark(v_sz-1,h_idx)

        for v_idx in range(0, v_sz):
            mark(v_idx, 0)
            mark(v_idx,h_sz-1)

        for v_idx in range(0, v_sz):
            for h_idx in range(0, h_sz):
                if board[v_idx][h_idx]=='o':
                    board[v_idx][h_idx]='O'
                elif board[v_idx][h_idx]=='O':
                    board[v_idx][h_idx]='X'
