class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head.next:
            return head
        if m == 1:
            t, te = head, head.next
            for i in xrange(1, n):
                tem = te.next
                te.next = t
                t, te = te, tem
            head.next = te
            return t
        t = head
        for i in xrange(2, m):
            t = t.next
        before = t
        for i in xrange(0, n-m+2):
            t = t.next
        after = t
        t, te = before.next, before.next.next
        while te != after:
            tem = te.next
            te.next = t
            t, te = te, tem
        before.next.next = after
        before.next = t
        return head
