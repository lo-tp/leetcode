class Solution(object):
    def rotateRight(self, head, k):
        res, end, sz = head, head, 1
        if head and k:
            while end and end.next:
                sz += 1
                end = end.next
            k %= sz
            if k:
                k = sz-k-1
                t = head
                while k:
                    t = t.next
                    k -= 1
                res = t.next
                t.next = None
                end.next = head
        return res

