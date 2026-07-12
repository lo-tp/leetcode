def getHeight(node: TreeNode) -> int:
    res = 0
    while node:
        res += 1
        node = node.left
    return res

def getNodeCount(root):
    if root:
        height,l,r=1,root.left, root.right
        while l and r:
            height+=1
            r,l=r.right, l.left
        if l or r:
            return getNodeCount(root.left)+getNodeCount(root.right)+1
        else:
            return 2**height-1
    return 0



class Solution(object):
    def countNodes(self, root):
        res, stack = 0, [root]
        while stack:
            tmp = []
            while stack:
                k = stack.pop()
                if k:
                    res += 1
                    tmp.append(k.left)
                    tmp.append(k.right)
            stack = tmp
        return res

    def countNodes(self, root: TreeNode) -> int:
        res, stack = 0, []
        while root or stack:
            if stack:
                stack.append(root)
                root = root.left
            else:
                res += 1
                root = stack.pop().right
        return res
    def countNodes(self, root: TreeNode) -> int:
        res = 0
        while root:
            l_height, r_height = getHeight(root.left), getHeight(root.right)
            res += 1
            if l_height == r_height:
                res += (1 << l_height)-1
                root = root.right
            else:
                res += (1 << r_height)-1
                root = root.left
        return res

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return getNodeCount(root)
