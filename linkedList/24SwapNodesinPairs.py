class Solution(object):
    def swapPairs(self, head):
        res = head
        if res and res.next:
            tmp, res = None, res.next
            stack = [(head, head.next, False)]
            while stack:
                node, prev_node, visited = stack.pop()
                if not visited:
                    tmp = node
                    if node and node.next:
                        stack.append((node, node.next, True))
                        a = node.next.next
                        node.next.next = node
                        stack.append((a, a.next if a else None, False))
                else:
                    node.next = tmp
                    tmp = prev_node
        return res
