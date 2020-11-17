class Solution(object):
    def invertTreeRecursive(self, root):
        if root:
            root.left=self.invertTree(root.right)
            root.right=self.invertTree(root.left)
        return root
    def invertTreeDFS(self, root):
        s=[]
        w=root
        while s or root:
            if root:
                s.append(root)
                root=root.left
            else:
                root=s.pop()
                k=root.left
                root.left=root.right
                root.right=k
                root=root.left
        return w
    def invertTreeBFS(self, root):
        s=[root]
        w=[]
        ret=root
        while s:
            while s:
                t=s.pop()
                if t:
                    k=t.left
                    t.left=t.right
                    t.right=k
                    w.append(t.left)
                    w.append(t.right)
            k=s
            s=w
            w=k
        return ret
    def invertTree(self, root):
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = root
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
