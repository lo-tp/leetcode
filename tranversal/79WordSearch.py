class Solution(object):
    def find(self, columnIndex, rowIndex, index):
        if index == len(self.word):
            return True
        if columnIndex >= 0 and columnIndex < self.columnSz and rowIndex >= 0 and rowIndex < self.rowSz and self.board[columnIndex][rowIndex] == self.word[index]:
            self.board[columnIndex][rowIndex] = None
            index += 1
            if self.find(columnIndex, rowIndex-1, index) or self.find(columnIndex, rowIndex+1, index) or self.find(columnIndex+1, rowIndex, index) or self.find(columnIndex-1, rowIndex, index):
                return True
            self.board[columnIndex][rowIndex] = self.word[index-1]
        return False

    def exist(self, board, word):
        self.board, self.word, self.columnSz = board, word, len(board)
        if self.columnSz:
            self.rowSz, columnIndex, rowIndex = len(board[0]), 0, 0
            while columnIndex < self.columnSz:
                rowIndex = 0
                while rowIndex < self.rowSz:
                    if self.find(columnIndex, rowIndex, 0):
                        return True
                    rowIndex += 1
                columnIndex += 1
        return False

    def existWithoutRecursion(self, board, word):
        wordSz, columnSz = len(word), len(board)
        if columnSz:
            rowSz = len(board[0])
            if rowSz:
                stack = []
                for column in xrange(0, columnSz):
                    for row in xrange(0, rowSz):
                        stack.append((column, row, 0, False))
                while stack:
                    (v, h, i, flag) = stack.pop()
                    if i == wordSz:
                        return True
                    # When the last element is true, then we should revert the modification we made to the data
                    elif flag:
                        board[v][h] = word[i]
                    elif v < columnSz and v >= 0 and h < rowSz and h >= 0 and board[v][h] == word[i]:
                        stack.append((v, h, i, True))
                        i += 1
                        board[v][h] = None
                        stack.append((v-1, h, i, False))
                        stack.append((v, h-1, i, False))
                        stack.append((v, h+1, i, False))
                        stack.append((v+1, h, i, False))
                return False


s = Solution()
print s.findMedianSortedArrays([], [1])
