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

