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
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        ret = None
        if t1 is not None and t2 is not None:
            ret = TreeNode(t1.val + t2.val)
            ret.left = self.mergeTrees(t1.left,t2.left);
            ret.right = self.mergeTrees(t1.right,t2.right);
        elif t1 is not None:
            ret = TreeNode(t1.val)
            ret.left = self.mergeTrees(t1.left,None);
            ret.right = self.mergeTrees(t1.right,None);
        elif t2 is not None:
            ret = TreeNode(t2.val)
            ret.left = self.mergeTrees(t2.left,None);
            ret.right = self.mergeTrees(t2.right,None);
        return ret;

soluction = Solution()
print soluction.mergeTrees(root,root).val
