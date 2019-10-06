class Solution(object):
    def splitListToParts(self, root, k):
        size, tmp = 0, root
        while tmp:
            size += 1
            tmp = tmp.next
        if k >= size:
            tmp, res = 0, [None for _ in xrange(0, k)]
            while root:
                res[tmp] = root
                root = root.next
                tmp += 1
            for i in [r for r in res if r]:
                r.next = None
            return res
        else:
            tmp = size/k
            tem = [tmp for i in xrange(0, k)]
            for i in xrange(0, size % k):
                tem[i] += 1
            res = [ListNode() for _ in xrange(0, k)]
            for index, i in tem:
                res[index] = root
                for j in xrange(1, i):
                    root = root.next
                tmp = root.next
                root.next = None
                root = tmp
            return res
