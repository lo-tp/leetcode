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
