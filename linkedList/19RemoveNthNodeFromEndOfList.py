class Solution(object):
    def removeNthFromEndUsingLessRAM(self, head, n):
        tmp, data = head, [head]
        while tmp:
            data.append(tmp.next)
            tmp = tmp.next
        sz = len(head)
        if n == sz:
            head = head.next
        else:
            data[sz-n-1].next = data[sz-n].next
        return head
    def removeNthFromEnd(self, head, n):
        data, i, k = {}, 1, head
        while k:
            data[i] = k
            k = k.next
            i += 1
        if n+1 == i:
            return head.next
        data[i] = None
        data[n-1].next = data[i+1]
        return head
    def removeNthFromEnd(self, head, n):
        te = prev = ListNode(0)
        prev.next = head
        t = head
        for _ in range(0, n):
            t = t.next
        while t:
            t = t.next
            te = te.next
        te.next = te.next.next
        return prev.next
