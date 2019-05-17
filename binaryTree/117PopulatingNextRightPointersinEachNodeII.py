class Solution(object):
    def connect(self, root):
        tmp = root
        while tmp:
            head = tmp
            prev_right = None
            while head:
                if head.left and head.right:
                    head.left.next = head.right
                    if prev_right:
                        prev_right.next = head.left
                    prev_right = head.right
                elif head.left:
                    if prev_right:
                        prev_right.next = head.left
                    prev_right = head.left
                elif head.right:
                    if prev_right:
                        prev_right.next = head.right
                    prev_right = head.right
                head = head.next
            while not tmp.left and not tmp.right and tmp.next:
                tmp = tmp.next
            tmp = tmp.left if tmp.left else tmp.right
        return root
