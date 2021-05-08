class Solution(object):

    def getTargetCopyBFS(self, original, cloned, target):
        a, b, c, d = [original], [], [cloned], []
        while a:
            while a:
                i, j = a.pop(), c.pop()
                if i == target:
                    return j
                if i.left:
                    b.append(i.left)
                    d.append(j.left)
                if i.right:
                    b.append(i.right)
                    d.append(j.right)
            a, b, c, d = b, a, d, c

    def getTargetCopyBFSZigzag(self, original, cloned, target):
        a, b, c, d, flag = [original], [], [cloned], [], True
        while a:
            while a:
                i, j = a.pop(), c.pop()
                if i == target:
                    return j
                if flag:
                    if i.left:
                        b.append(i.left)
                        d.append(j.left)
                    if i.right:
                        b.append(i.right)
                        d.append(j.right)
                else:
                    if i.right:
                        b.append(i.right)
                        d.append(j.right)
                    if i.left:
                        b.append(i.left)
                        d.append(j.left)
            a, b, c, d, flag = b, a, d, c, not flag

    def getTargetCopyDfsPreOrder(self, original, cloned, target):
        s1, s2 = [], []
        while s1 or original:
            if original:
                if original == target:
                    return cloned
                s1.append(original)
                original = original.left
                s2.append(cloned)
                cloned = cloned.left
            else:
                original = s1.pop().right
                cloned = s2.pop().right

    def getTargetCopyDfsInOrder(self, original, cloned, target):
        s1, s2 = [], []
        while s1 or original:
            if original:
                s1.append(original)
                original = original.left
                s2.append(cloned)
                cloned = cloned.left
            else:
                original = s1.pop()
                cloned = s2.pop()
                if original and original == target:
                    return cloned
                original = original.right
                cloned = cloned.right

    def getTargetCopyDfsPostOrder(self, original, cloned, target):
        s1, s2 = [], []
        while s1 or original:
            if original:
                s1.append((original, False))
                original = original.left
                s2.append((cloned, False))
                cloned = cloned.left
            else:
                original, o_flag = s1.pop()
                cloned, c_flag = s2.pop()
                if not o_flag:
                    s1.append((original, True))
                    s2.append((cloned, True))
                    original = original.right
                    cloned = cloned.right
                elif original and original == target:
                    return cloned
                else:
                    original = False
    def getTargetCopyMorrisPreOrder(self, original, cloned, target):
        res = None
        while original:
            if original.left:
                m, t = cloned.left, original.left
                while t.right and t.right != original:
                    t = t.right
                    m = m.right
                if t.right:
                    original, cloned = original.right, cloned.right
                    t.right = None
                    m.right = None
                else:
                    t.right = original
                    m.right = cloned
                    if original == target:
                        res = cloned
                    original, cloned = original.left, cloned.left
            else:
                if original == target:
                    res = cloned
                original, cloned = original.right, cloned.right
        return res
    def getTargetCopyMorrisInOrder(self, original, cloned, target):
        res = None
        while original:
            if original.left:
                m, t = cloned.left, original.left
                while t.right and t.right != original:
                    t = t.right
                    m = m.right
                if t.right:
                    if original == target:
                        res = cloned
                    original, cloned = original.right, cloned.right
                    t.right = None
                    m.right = None
                else:
                    t.right = original
                    m.right = cloned
                    original, cloned = original.left, cloned.left
            else:
                if original == target:
                    res = cloned
                original, cloned = original.right, cloned.right
        return res

