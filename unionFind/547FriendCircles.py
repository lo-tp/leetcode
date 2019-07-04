class UF():
    def __init__(self, size):
        self.root = [-1]*size
        self.count = 0

    def find(self, target):
        if self.root[target] != -1:
            tmp = target
            while tmp != self.root[tmp]:
                tmp = self.root[tmp]
            return tmp
        return -1

    def merge(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == -1 and root_b == -1:
            self.root[a] = self.root[b] = b
            self.count += 1
        elif root_a == -1:
            self.root[a] = root_b
        elif root_b == -1:
            self.root[b] = root_a
        elif a != b and root_a != root_b:
            self.root[root_a] = root_b
            self.count -= 1


class Solution(object):
    def findCircleNum(self, M):
        size = len(M)
        uf = UF(size)
        for column_index in xrange(0, size):
            for row_index in xrange(0, size):
                if M[column_index][row_index]:
                    uf.merge(column_index, row_index)
        return uf.count

