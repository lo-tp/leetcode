class CBTInserter:

    def __init__(self, root: TreeNode):
        flag, self.index, self.root, self.cur, self.next = False, 0, root, [
            root], []
        while True:
            for index, t in enumerate(self.cur):
                if t.left and t.right:
                    self.next.extend([t.left, t.right])
                else:
                    flag = True
                    self.index = index
                    if t.left:
                        self.next.append(t.left)
                    break
            if flag:
                break
            self.cur, self.next = self.next, []

    def insert(self, v: int) -> int:
        if self.index == len(self.cur):
            self.index, self.cur, self.next = 0, self.next, []
            return self.insert(v)
        cur_node = self.cur[self.index]
        if cur_node.left and cur_node.right:
            self.index += 1
            return self.insert(v)
        new_node = TreeNode(v)
        if cur_node.left:
            cur_node.right = new_node
        else:
            cur_node.left = new_node
        self.next.append(new_node)
        return cur_node.val

    def get_root(self) -> TreeNode:
        return self.root
