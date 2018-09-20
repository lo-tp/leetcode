class Solution(object):
    def convertBST(self, root):
        sum=0
        ret=root
        s=[]
        while s or root:
            if root:
                s.append(root)
                root=root.right
            else:
                root=s.pop()
                sum+=root.val
                root.val=sum
                root=root.left
        return ret
