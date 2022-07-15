from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepthTLE(self, root: Optional[TreeNode]) -> int:
        if root:
            q = deque()
            q.append((root, 1))
            while q:
                t, dp = q.popleft()
                if not t.left and not t.right:
                    return dep
                dep += 1
                if t.left:
                    q.append((t.left, dep))
                if t.right:
                    q.append((t.right, dep))
        return 0

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            q = deque()
            q.append((root, 1))
            while q:
                t, dep = q.popleft()
                if not t.left and not t.right:
                    return dep
                dep += 1
                if t.left:
                    q.append((t.left, dep))
                if t.right:
                    q.append((t.right, dep))
        return 0
