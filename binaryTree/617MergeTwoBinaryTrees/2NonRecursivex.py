# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        root = TreeNode(None)
        stack1 = []
        stack2 = []
        stack3 = []
        stack3.append(root)
        if t1 is not None:
            stack1.append(t1)
        else:
            stack1.append(None)
        if t2 is not None:
            stack2.append(t2)
        else:
            stack2.append(None)
        while len(stack3):
            node1 = stack1.pop()
            node2 = stack2.pop()
            node3 = stack3.pop()
            if node1 is None:
                node3.val = node2.val
                if node2.left is not None:
                    node3.left = TreeNode(None)
                    stack2.append(node2.left)
                    stack1.append(None)
                    stack3.append(node3.left)
                if node2.right is not None:
                    node3.right = TreeNode(None)
                    stack2.append(node2.right)
                    stack1.append(None)
                    stack3.append(node3.right)
            elif node2 is None:
                node3.val = node1.val
                if node1.left is not None:
                    node3.left = TreeNode(None)
                    stack1.append(node1.left)
                    stack2.append(None)
                    stack3.append(node3.left)
                if node1.right is not None:
                    node3.right = TreeNode(None)
                    stack1.append(node1.right)
                    stack2.append(None)
                    stack3.append(node3.right)
            else:
                node3.val = node1.val + node2.val
                if node1.left is not None or node2.left is not None:
                    node3.left=TreeNode(None)
                    stack1.append(node1.left)
                    stack2.append(node2.left)
                    stack3.append(node3.left)
                if node1.right is not None or node2.right is not None:
                    node3.right=TreeNode(None)
                    stack1.append(node1.right)
                    stack2.append(node2.right)
                    stack3.append(node3.right)
        return root

soluction = Solution()
print soluction.mergeTrees(root,root).val
