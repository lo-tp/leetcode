class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        s1=[]
        s2=[]
        s3=[]
        t3=t1 or t2
        ret=t3
        while t1 or s1 or t2 or s2:
            if t1 or t2:
                t3=t1 if t1 else t2
                s3.append(t3)
                s2.append(t2)
                s1.append(t1)
                t2= t2 and t2.left
                t1=t1 and t1.left
                t3.left=t2 or t1
                t3=t3.left
            else:
                t3=s3.pop()
                t2=s2.pop()
                t1=s1.pop()
                if t1 and t2:
                    t3.val=t1.val+t2.val
                t2=t2 and t2.right
                t1=t1 and t1.right
                t3.right=t2 or t1
                t3=t3.right
        return ret
