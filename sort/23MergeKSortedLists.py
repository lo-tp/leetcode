from Queue import PriorityQueue


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
    def mergeKListsButTLE(self, lists):
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

    def mergeKLists(self, lists):
        pq = PriorityQueue()
        prev = tmp = ListNode(None)
        for i in lists:
            if i:
                pq.put((i.val, i))
        while not pq.empty():
            (_, node) = pq.get()
            tmp.next = node
            tmp = tmp.next
            if tmp.next:
                pq.put((tmp.next.val, tmp.next))
        return prev.next
