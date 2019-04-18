def findMiddleNode(head, end):
    quickPointer = head
    while quickPointer != end and quickPointer.next != end:
        head = head.next
        quickPointer = quickPointer.next.next
    return head


def mergeSort(head, end):
    mid = findMiddleNode(head, end)
    tmp, left, right = ListNode(0), mergeSort(head, mid), mergeSort(mid, end)
    res = tmp
    while left != mid and right != end:
        if left.val < right.val:
            tmp.next = left
            left = left.next
        else:
            tmp.next = right
            right = right.next
        tmp = tmp.next
    while left != mid:
        tmp.next = left
        left = left.next
        tmp = tmp.next
    while right != end:
        tmp.next = right
        right = right.next
        tmp = tmp.next
    tmp.next = right
    return res.next


class Solution(object):
    def sortList(self, head):
        return mergeSort(head, None)

