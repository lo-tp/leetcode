from Queue import PriorityQueue
from collections import deque


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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists=deque(lists)
        while len(lists)>1:
            t1,t2=lists.popleft(),lists.popleft()
            new_list=tmp=ListNode(0)
            while t1 and t2:
                if t1.val>t2.val:
                    tmp.next=t2
                    t2=t2.next
                    tmp=tmp.next
                else:
                    tmp.next=t1
                    t1=t1.next
                    tmp=tmp.next
            if t1 or t2:
                tmp.next=t1 if t1 else t2
            lists.append(new_list.next)
        return lists[0] if lists else None
