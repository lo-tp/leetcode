class Solution(object):
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
