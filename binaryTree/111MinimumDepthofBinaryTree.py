from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            dep, cur, tmp = 0, [root], []
            while cur:
                dep += 1
                for c in cur:
                    if not c.left and not c.right:
                        return dep
                    if c.left:
                        tmp.append(c.left)
                    if c.right:
                        tmp.append(c.right)
                tmp, cur = cur, tmp
        return 0
