class Solution(object):
    def getTreeData(self, t):
        ret=[]
        s=[]
        while s or t:
            if t:
                s.append(t)
                t=t.left
            else:
                t=s.pop()
                ret.append(t.val)
                t=t.right
                if t:
                    ret.append(None)
        return ret

    def isSameTree(self, p, q):
        retP=self.getTreeData(p)
        retQ=self.getTreeData(q)
        size=len(retQ)
        if size!=len(retP):
            return False
        for i in xrange(0, size):
            if retP[i]!=retQ[i]:
                return False
        return True

class Solution(object):
    def isSameTree(self, p, q):
        sq=[]
        sp=[]
        while (p and q) or (sq and sp):
            if p and q:
                sq.append(q)
                sp.append(p)
                p=p.left
                q=q.left
            elif (not p and not q):
                p=sp.pop()
                q=sq.pop()
                if p.val!=q.val:
                    return False
                p=p.right
                q=q.right
            else:
                return False
        if sp or sq or p or q:
            return False
        return True
