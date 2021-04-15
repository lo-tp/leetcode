def sortedArrayToBST(nums):
    res = None
    if nums:
        stack = [(None, 0, len(nums)-1, 0)]
        while stack:
            node, l, r, flag = stack.pop()
            if l <= r:
                m = int(l+(r-l)/2)
                if not flag:
                    node = TreeNode(nums[m])
                    stack.append((node, l, r, 1))
                    stack.append((None, l, m-1, 0))
                elif flag == 1:
                    node.left = res
                    stack.append((node, l, r, 2))
                    stack.append((None, m+1, r, 0))
                else:
                    node.right = res
            res = node
    return res


class Solution(object):
    def sortedListToBST(self, head):
        data = []
        while head:
            data.append(head.val)
            head = head.next
        return sortedArrayToBST(data)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        t, sz = head, -1
        while t:
            sz += 1
            t = t.next
        stack, prev_node = [(0, sz, 0, None)], None
        while stack:
            start, end, flag, node = stack.pop()
            m = int(start+(end-start)/2)
            if end >= start:
                if not flag:
                    stack.extend(
                        [(start, end, 1, None), (start, m-1, 0, None)])
                elif flag == 1:
                    node = TreeNode(head.val)
                    node.left = prev_node
                    head = head.next
                    stack.extend([(start, end, 2, node), (m+1, end, 0, None)])
                else:
                    node.right = prev_node
            prev_node = node
        return prev_node
