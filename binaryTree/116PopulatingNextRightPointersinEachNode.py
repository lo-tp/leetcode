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

