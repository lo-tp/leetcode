class Solution(object):
    def partition(self, head, x):
        lo, hi = ListNode(0), ListNode(0)
        lo1, hi1 = lo, hi
        while head:
            if head.val < x:
                lo.next = head
                lo = lo.next
            else:
                hi.next = head
                hi = hi.next
            head = head.next
        hi.next = None
        lo.next = hi1.next
        return lo1.next
