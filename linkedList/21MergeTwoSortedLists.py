class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head=ListNode(1)
        tmp=head
        while l1 and l2:
            if l1.val < l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
        if l1:
            head.next=l1
        if l2:
            head.next=l2
        return tmp.next
