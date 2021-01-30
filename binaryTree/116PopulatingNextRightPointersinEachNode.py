def getEnds(node, is_left, prev):
    if node:
        prev.append(node)
        getEnds(node.left if is_left else node.right, is_left, prev)
    return prev


def height(node):
    return max(height(node.left), height(node.right))+1 if node else 0


def traverse(node, level):
    if node:
        if level == 0:
            left_ends, right_ends = getEnds(
                node.left, False, []), getEnds(node.right, True, [])
            for i in xrange(0, len(left_ends)):
                left_ends[i].next = right_ends[i]
        else:
            level -= 1
            traverse(node.left, level)
            traverse(node.right, level)


class Solution(object):
    def connect(self, root):
        for i in xrange(0, height(root)-1):
            traverse(root, i)
        return root
    def connectNonRecursice(self, root):
        pre = root
        while pre and pre.left:
            head = pre
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            pre = pre.left
        return root

    def connect(self, root):
        stack = []
        if root:
            stack.append(root)
        reverse = False
        while stack:
            tmp = []
            while stack:
                node = stack.pop()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                if stack:
                    node.next = stack[-1]
            stack, tmp = tmp, stack
            while stack:
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
                if stack:
                    stack[-1].next = node
            stack = tmp
        return root


    def connect(self, root):
        stack, tmp = [], []
        if root:
            stack.append(root)
        while stack:
            while stack:
                node = stack.pop()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                if stack:
                    node.next = stack[-1]
            stack, tmp = tmp, stack
            while stack:
                node = stack.pop()
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
                if stack:
                    stack[-1].next = node
            stack, tmp = tmp, stack
        return root
