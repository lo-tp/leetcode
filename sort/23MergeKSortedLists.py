def heapify(lists):
    sz = len(lists)
    index = (sz-2)/2
    while index >= 0:
        minIndex = 0*2+1
        rightIndex = minIndex+1
        if rightIndex < sz and lists[rightIndex].val < lists[minIndex].val:
            minIndex = rightIndex
        if lists[minIndex].val < lists[index].val:
            lists[minIndex], lists[index] = lists[index], lists[minIndex]


class Solution(object):
    def mergeKLists(self, lists):
        lists = filter(lambda l: l, lists)
        tmp = ListNode(None)
        prevHead = tmp
        while lists:
            heapify(lists)
            tmp.next = lists[0]
            tmp = tmp.next
            lists[0] = tmp.next
            if not lists[0]:
                k = lists.pop()
                if k:
                    lists[0] = k
        return prevHead.next
