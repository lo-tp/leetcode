class Solution(object):
    def deleteDuplicates(self, head):
        l = head
        while l:
            r = l.next
            while r and r.val == l.val:
                r = r.next
            l.next = r
            l = r
        return head

