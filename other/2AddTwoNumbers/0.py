class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret=l1
        addOne=False
        while l1.next and l2.next:
            l1.val+=l2.val
            if addOne:
                l1.val+=1
            if l1.val>9:
                l1.val%=10
                addOne=True
            else:
                addOne=False
            l1=l1.next
            l2=l2.next
        if l2.next:
            l1.next=l2.next
        l1.val+=l2.val
        if addOne:
            l1.val+=1
        if l1.val>9:
            l1.val%=10
            addOne=True
        else:
            addOne=False
        while l1 and l1.next and addOne:
            l1=l1.next
            l1.val+=1
            if l1.val>9:
                l1.val%=10
                addOne=True
            else:
                addOne=False
        if addOne:
            l1.next=ListNode(1)
