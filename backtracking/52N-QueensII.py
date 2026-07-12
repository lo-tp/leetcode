class Solution(object):
    def totalNQueens(self, sz):
        res, remain = 0, [
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
                for i, j in affect[index][val]:
                    remain[i][j] -= 1
            else:
                stack.append((val, True))
                for i, j in affect[index][val]:
                    remain[i][j] += 1
                index += 1
                if index == sz:
                    res += 1
                else:
                    stack.extend([(i, False)
                                  for i in xrange(0, sz) if not remain[index][i]])
        return res


    def totalNQueens(self, n: int) -> int:
        res,horizontal_index, index_sum, index_diff=0,set(),set(),set()
        stack=[(0,i, False) for i in range(0,n)]
        while stack:
            i,j, visited=stack.pop()
            if visited:
                horizontal_index.remove(j)
                index_sum.remove(i+j)
                index_diff.remove(i-j)
            else:
                if len(horizontal_index)==n-1:
                    res+=1
                    continue
                horizontal_index.add(j)
                index_sum.add(i+j)
                index_diff.add(i-j)
                stack.append((i, j, True))
                i+=1
                for t in range range(0,n):
                    if not t in horizontal_index and not i+t in index_sum and not i-t in index_diff:
                        stack.append((i,t,False))
        return res
