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


s = Solution()
print s.findMedianSortedArrays([], [1])
