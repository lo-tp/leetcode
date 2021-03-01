class Solution(object):
    def buildTree(self, inorder, postorder):
        prev_sz, cur, stack = 0, None, [(0, 0, len(inorder), None, 0)]
        while stack:
            in_s, post_s, sz, node, flag = stack.pop()
            if not sz:
                cur = None
            elif not flag:
                next_sz = 0
                for i in range(0, sz):
                    if inorder[in_s+i] == postorder[post_s+sz-1]:
                        next_sz = i
                        break
                cur = TreeNode(postorder[post_s+sz-1])
                stack.append(
                    (in_s, post_s, sz, cur, 1))
                stack.append((in_s, post_s, next_sz, None, 0))
            elif flag == 1:
                node.left = cur
                stack.append((in_s, post_s, sz, node, 2))
                cur = node
                stack.append(
                    (in_s+prev_sz+1, post_s+prev_sz, sz-prev_sz-1, None, 0))
            else:
                node.right = cur
                cur = node
            prev_sz = sz
        return cur

    def buildTree(self, inorder, postorder):
        prev_sz, prev_node, sz = 0, None, len(inorder)
        stack = [(0, 0, sz, prev_node, 0)]
        while stack:
            in_start, post_start, size, node, flag = stack.pop()
            if not size:
                node = None
            elif not flag:
                post_index = post_start+size-1
                node = TreeNode(postorder[post_index])
                stack.append((in_start, post_start, size, node, 1))
                i = 0
                while inorder[in_start+i] != node.val:
                    i += 1
                stack.append((in_start, post_start, i, None, 0))
            elif flag == 1:
                node.left = prev_node
                stack.append((in_start, post_start, size, node, 2))
                stack.append((in_start+prev_sz+1, post_start +
                              prev_sz, size-1-prev_sz, None, 0))
            else:
                node.right = prev_node
            prev_sz, prev_node = size, node
        return prev_node
