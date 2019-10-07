class Solution(object):
    def splitListToParts(self, root, k):
        tem, res, size, tmp = [1]*k, [None]*k, 0, root
        while tmp:
            size += 1
            tmp = tmp.next
        for i in xrange(size, k):
            tem[i] = 0
        if k < size:
            tmp = size/k
            tem = [tmp]*k
            for i in xrange(0, size % k):
                tem[i] += 1
        for index, i in enumerate(tem):
            if(i):
                res[index] = root
                for j in xrange(1, i):
                    root = root.next
                tmp = root.next
                root.next = None
                root = tmp
        return res
