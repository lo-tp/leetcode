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
