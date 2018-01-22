
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)

class Solution(object):
    def tree2str(self, t1):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        str=''
        if t1 is not None:
            str="%d" % (t1.val)
            if t1.left is not None and t1.right is not None:
                str=("%s(%s)(%s)" % (str, self.tree2str(t1.left),self.tree2str(t1.right)))
            elif t1.left is not None:
                str=("%s(%s)" % (str, self.tree2str(t1.left)))
            elif t1.right is not None:
                str=("%s()(%s)" % (str, self.tree2str(t1.right)))
        return str

soluction = Solution()
print soluction.tree2str(root)
