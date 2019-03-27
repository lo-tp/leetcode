from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        if root:
            s = deque()
            s.append(root.left)
            s.append(root.right)
            while len(s) > 1:
                lQ = deque(), rQ = deque()
                while len(s) > 1:
                    l, r = s.popleft(), s.pop()
                    if l and r and l.val == r.val:
                        lQ.append(l.left)
                        lQ.append(l.right)
                        rQ.appendleft(r.right)
                        rQ.appendleft(r.left)
                    elif l or r:
                        return False
                if len(s) > 0:
                    return False
                s = lQ
                s.extend(rQ)
                if len(s) % 2:
                    return False
        return True
