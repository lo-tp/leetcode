class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        quick=head
        slow=head
        while head:
            quick=quick.next
            if not quick:
                return False
            if quick==slow:
                return True
            quick=quick.next
            if not quick:
                return False
            if quick==slow:
                return True
            slow=slow.next
        return False
