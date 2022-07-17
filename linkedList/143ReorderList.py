from typing import List, Optional
from math import floor


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
