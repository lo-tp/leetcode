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
    def swapPairs(self, head):
        res = head
        if res and res.next:
            tmp, res = None, res.next
            stack = [(head, head.next, False)]
            while stack:
                node, prev_node, visited = stack.pop()
                if not visited:
                    tmp = node
                    if node and node.next:
                        stack.append((node, node.next, True))
                        a = node.next.next
                        node.next.next = node
                        stack.append((a, a.next if a else None, False))
                else:
                    node.next = tmp
                    tmp = prev_node
        return res
    def swapPairs(self, head):
        return self.reverseKGroup(head,2)
