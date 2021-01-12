def help(head, k):
    t = head
    for _ in range(0, k-1):
        if t:
            t = t.next
    if t:
        te, tem = head, head.next
        head.next = t.next
        while te != t:
            temp = tem.next
            tem.next = te
            te, tem = tem, temp
        head = t
    return head

def helper(start, k):
    t = start
    for _ in range(0, k):
        if not t:
            return (start, None)
        t = t.next
    l, r = start, start.next
    while r != t:
        te = r.next
        r.next = l
        l, r = r, te
    start.next = t
    return (l, start)

def reverse(head, k):
    l, r = head, head.next
    for i in range(0, k):
        t = r.next
        r.next = l
        l, r = r, t
    return (l, head, r)

def isReversable(head,k):
    for i in range(0,k):
        if head:
            head=head.next
        else:
            return False
    return True

class Solution(object):
    def reverseKGroup(self, head, k):
        k -= 1
        l = head
        for i in range(0, k):
            if l:
                l = l.next
            else:
                break
        if l:
            head, r, next_node = reverse(head, k)
            while True:
                l = next_node
                for i in range(0, k):
                    if l:
                        l = l.next
                    else:
                        break
                if l:
                    l, r1, t = reverse(next_node, k)
                    r.next, next_node = l, t
                    r = r1
                else:
                    r.next = next_node
                    break
        return head
    def reverseKGroup(self, head, k):
        te=k
        k -= 1
        l = head
        if isReversable(head,te):
            head, r, next_node = reverse(head, k)
            while True:
                l = next_node
                if isReversable(l, te):
                    l, r1, t = reverse(next_node, k)
                    r.next, next_node = l, t
                    r = r1
                else:
                    r.next = next_node
                    break
        return head
    def reverseKGroup(self, head, k):
        ret = prev = ListNode(0)
        prev.next = head
        while True:
            l, r = helper(prev.next)
            if l == prev.next:
                break
            prev.next = l
            prev = r
        return ret.next

    def reverseKGroup(self, head, k):
        res = p = ListNode(0)
        p.next = head
        while True:
            t, te = p.next, help(p.next, k)
            if te == t:
                break
            p, p.next = t, te
        return res.next
