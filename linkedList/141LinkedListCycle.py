class Solution(object):
    def hasCycle(self, head):
        f = head.next if head else head
        while f and f.next:
            if f == head:
                return True
            head = head.next
            f = f.next.next
        return False

   def hasCycle(self, head):
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        quick = head
        slow = head
        while head:
            quick = quick.next
            if not quick:
                return False
            if quick ==slow:
                return True
            quick = quick.next
            if not quick:
                return False
            if quick ==slow:
                return True
            slow = slow.next
        return False
