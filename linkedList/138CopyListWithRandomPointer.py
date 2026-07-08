class Solution(object):
    def copyRandomListBetter(self, head):
        if head:
            tem = head
            while tem:
                tem.next = Node(tem.val, tem.next, None)
                tem = tem.next.next
            tem, tmp = head, head.next
            while tem:
                if tem.random:
                    tem.next.random = tem.random.next
                tem = tem.next.next

            tem = head
            temp = head.next
            while tem:
                tem.next = tem.next.next
                if tmp.next:
                    tmp.next = tmp.next.next
                tem, tmp = tem.next, tmp.next
            return temp
        return None
    def copyRandomList(self, head):
        tem, tmp = head, Node(0, None, None)
        temp = tmp
        while tem:
            tmp.next = Node(tem.val, None, None)
            tem, tmp = tem.next, tmp.next
        tem, tmp = head, temp.next
        while tem:
            if tem.random:
                t, k = head, temp.next
                while t != tem.random:
                    t, k = t.next, k.next
                tmp.random = k
            tem, tmp = tem.next, tmp.next
       return temp.next
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            t=head
            while t:
                te=t.next
                t.next=Node(next=te, x=t.val)
                t=te
            t=head
            while t:
                if t.random:
                    t.next.random=t.random.next
                if t.next:
                    t=t.next.next
            res=head.next
            original, copied, index=Node(x=0),Node(x=0),0
            while head:
                if index%2:
                    copied.next=head
                    copied=copied.next
                else:
                    original.next=head
                    original=original.next
                t=head.next
                head.next=None
                head=t
                index+=1
            return res
        return None
