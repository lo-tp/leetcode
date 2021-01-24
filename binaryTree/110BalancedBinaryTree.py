def getHeight(root):
    if not root:
        return 0
    l_h, r_h = getHeight(root.left), getHeight(root.right)
    if l_h != -1 and r_h != -1 and abs(l_h-r_h) < 2:
        return max(l_h, r_h)+1
    return -1
class Solution(object):
    def isBalanced(self, root):
        h, stack = 0, [[root, -1]]
        while stack:
            cur, left_h = stack[-1]
            if cur:
                if left_h == -1:
                    stack[-1][1] = -2
                    stack.append([cur.left, -1])
                elif left_h == -2:
                    stack[-1][1] = h
                    stack.append([cur.right, -1])
                else:
                    if abs(left_h-h) > 1:
                        return False
                    h = max(left_h, h)+1
                    stack.pop()
            else:
                h = 0
                stack.pop()
        return True

    def isBalanced(self, root):
        if not root:
            return True
        l_h, r_h = getHeight(root.left), getHeight(root.right)
