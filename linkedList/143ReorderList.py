from typing import List, Optional


def findMiddlePoint(head: ListNode):
    slow, quick = head, head
    while quick.next and quick.next.next:
        slow = slow.next
        quick = quick.next.next
    return slow.next if quick.next else slow


def reverseList(head: ListNode):
    p, n = head, head.next
    head.next = None
    while n:
        i = n.next
        n.next = p
        p, n = n, i
    return p


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        t, arr = head, []
        while t:
            arr.append(t)
            t = t.next
        count, l, r = 1, 0, len(arr) - 1
        while l < r:
            if count % 2:
                arr[l].next = arr[r]
                l += 1
            else:
                arr[r].next = arr[l]
                r -= 1
            count += 1
        arr[floor(len(arr) / 2)].next = None
        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head:
            mid = findMiddlePoint(head)
            reversed = reverseList(mid)
            t = head
            while t != mid:
                i, j = t.next, reversed.next
                t.next = reversed
                reversed.next = i
                t, reversed = i, j
            mid.next = None
