def reverse(head, k):
    l, r = head, head.next
    for i in range(0, k):
        t = r.next
        r.next = l
        l, r = r, t
    return (l, head, r)


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
