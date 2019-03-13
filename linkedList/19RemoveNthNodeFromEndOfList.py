class Solution(object):
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
