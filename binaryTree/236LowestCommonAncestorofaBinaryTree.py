class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        tmp, stack = 0, [[None, root]]
        while stack:
            [left_match_num, current_node] = stack[-1]
            if current_node:
                if left_match_num == None:
                    stack[-1][0] = 'a'
                    stack.append([None, current_node.left])
                elif left_match_num == 'a':
                    stack[-1][0] = tmp
                    stack.append([None, current_node.right])
                else:

                    sum = left_match_num+tmp
                    if current_node.val == p.val or current_node.val == q.val:
                        sum += 1
                    if sum == 2:
                        return current_node
                    tmp = sum
                    stack.pop()
            else:
                tmp = 0
                stack.pop()
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cache={}
        cache[None]=0
        stack=[(root, False)]
        while stack:
            node, visited=stack.pop()
            if node:
                if visited:
                    cache[node]=cache[node.left]+cache[node.right]
                    if node==p or node==q:
                        cache[node]+=1
                    if cache[node]==2:
                        return node
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack, parent=[root], {}
        while stack:
            t=stack.pop()
            if t.left:
                parent[t.left]=t
                stack.append(t.left)
            if t.right:
                parent[t.right]=t
                stack.append(t.right)
        p_parent_path=set([root])
        while p in parent:
            p_parent_path.add(p)
            p=parent[p]
        while not q in p_parent_path:
            q=parent[q]
        return q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q:
            return root
        l,r=self.lowestCommonAncestor(root.left, p,q), self.lowestCommonAncestor(root.right, p,q)
        if l and r:
            return root
        return l if l else r
