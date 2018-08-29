class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ret,addone=l1,False
        addOne=False
        while l1.next and l2:
            k=l1.val+l2.val
            if addOne:
              k+=1
            addOne = k>=10
            l1.val=k%10
            l1=l1.next
            l2=l2.next
        if addOne:
            l1.val=l1.val+1
        if l2:
            l1.val+=l2.val
            l1.next=l2.next
        addOne=l1.val>=10
        l1.val%=10
        while l1.next and addOne:
            l1=l1.next
            l1.val+=1
            addOne=l1.val>=10
            l1.val%=10
        if addOne:
            l1.next=ListNode(1)
        return ret
