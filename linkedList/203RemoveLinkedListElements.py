class Solution(object):
    def removeElements(self, head, val):
        tem = tmp = ListNode(1)
        tmp.next = head
        while tmp and tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return tem.next
