from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            sz=len(q)
            total=0
            for _ in range(0,sz):
                n=q.popleft()
                total+=n.val;
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(total/sz)
        return res
    def averageOfLevelsDFS(self, root: Optional[TreeNode]) -> List[float]:
        totals = []
        counts = []
        
        def dfs(node, depth):
            if not node:
                return
                
            # If we are visiting this depth for the very first time, initialize our arrays
            if depth == len(totals):
                totals.append(node.val)
                counts.append(1)
            else:
                # Otherwise, add to the existing sum and increment the node count
                totals[depth] += node.val
                counts[depth] += 1
                
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 0)
        
        # Calculate the average for each level by dividing total sum by node count
        return [t / c for t, c in zip(totals, counts)]

    def __init__(self):
        self.res=[]
    def dfs(root, depth):
        if root:
            if len(self.res)==depth:
                self.res.append([])
            self.res[depth].append(root.val)
            self.dfs(root.left, depth+1)
            self.dfs(root.right, depth+1)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.dfs(root,0)
        return [(sum(t)/len(t) for t in res]

