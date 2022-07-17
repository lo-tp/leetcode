from typing import List, Optional


def reverseList(head: ListNode):
    if head.next:
        newHead, t = reverseList(head.next)
        t.next = head
        return newHead, head
    return head, head


class Solution(object):
    def reverseList(self, head):
        if head:
            i, j = head, head.nex
            while j:
                t = j.next
                j.next = i
                i, j = j, t
            head.next = None
            return i
        return head
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            res = reverseList(head)[0]
            head.next = None
            return res
