class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow=head
        quick=head.next
        shouldSlowGo=True
        while quick and quick!=slow:
            quick=quick.next
            if quick:
                quick=quick.next
            else:
                return None
            slow=slow.next
        if not quick:
            return None
        slow=head
        quick=quick.next
        while quick!=slow:
            quick=quick.next.next
            slow=slow.next
        return quick
