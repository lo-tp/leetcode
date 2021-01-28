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
