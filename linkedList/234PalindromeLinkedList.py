def findMiddle(head, end):
    tmp = head
    while tmp != end and tmp.next != end:
        tmp = tmp.next.next
        head = head.next
    return (tmp != end, head)


def revertLinkedList(head, end):
    prev, next = head, head.next
    prev.next = None
    while next != end:
        tmp = next.next
        next.next = prev
        prev = next
        next = tmp
    return prev


class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        (odd, middle) = findMiddle(head, None)
        revert_first_half = revertLinkedList(head, middle)

        if odd:
            tmp = ListNode(middle.val)
            tmp.next = revert_first_half
            revert_first_half = tmp
        while revert_first_half:
            if revert_first_half.val != middle.val:
                return False
            revert_first_half = revert_first_half.next
            middle = middle.next
        return True


def findMiddle(head, end):
    tmp = head
    while tmp != end and tmp.next != end:
        tmp = tmp.next.next
        head = head.next
    return (tmp != end, head)
