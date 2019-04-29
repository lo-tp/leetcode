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

