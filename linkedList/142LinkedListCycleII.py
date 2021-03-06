class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        quick=head
        slow=head
        while quick and quick.next:
            quick=quick.next.next
            slow=slow.next
            if quick==slow:
                break;
        if quick and quick.next:
            slow=head
            while slow!=quick:
                slow=slow.next
                quick=quick.next
                if(slow==quick):
                    break;
            return slow
        return None
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast and fast.next:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None

