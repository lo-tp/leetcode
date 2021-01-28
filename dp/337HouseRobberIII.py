class Solution(object):
    def dfs(self, root):
        if not root:
            return [0,0]
        else:
            l,r=self.dfs(root.left), self.dfs(root.right)
            return [root.val+l[1]+r[1], max(l)+max(r)]
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
    def rob(self, root):
        stack, t, te = [(root, 0, 0, 0)], 0, 0
        while stack:
            node, include, exclude, flag = stack.pop()
            if node:
                if not flag:
                    stack.append((node, node.val, exclude, 1))
                    stack.append((node.left, 0, 0, 0))
                elif flag == 1:
                    include += te
                    exclude += max(t, te)
                    stack.append((node, include, exclude, 2))
                    stack.append((node.right, 0, 0, 0))
                else:
                    include += te
                    exclude += max(t, te)
            t, te = include, exclude
        return max(t, te)
