from collections import defaultdict


class DLinkedList():
    def __init__(self, val, key):
        self.prev, self.next, self.val, self.key = None, None, val, key
def deleteNode(node):
    node.next.prev, node.prev.next = node.prev, node.next


def insertNode(head, node):
    node.prev, node.next = head, head.next
    head.next.prev = node
    head.next = node


class LRUCache(object):
    def debug(self):
        print('pre order')
        t = self.head
        while t:
            print(t.key, t.val)
            t = t.next
        print('post order')
        t = self.tail
        while t:
            print(t.key, t.val)
            t = t.prev

    def __init__(self, capacity):
        self.head, self.tail = DLinkedList(0, 'head'), DLinkedList(0, 'tail')
        self.head.next, self.tail.prev = self.tail, self.head
        self.hash, self.ration = defaultdict(lambda: None), capacity

    def get(self, key):
        node = self.hash[key]
        if node:
            node.prev.next, node.next.prev = node.next, node.prev
            # self.head.next, self.head.next.prev, node.next, node.prev = node, node, self.head.next, self.head
            node.next, node.prev = self.head.next, self.head.next.prev
            self.head.next.prev = node
            self.head.next = node
            return node.val
        return -1

    def put(self, key, value):
        node = self.hash[key]
        if node:
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
        else:
            node = DLinkedList(value, key)
            self.hash[key] = node
            if not self.ration:
                last_node = self.tail.prev
                self.tail.prev = last_node.prev
                self.hash[last_node.key] = None
            else:
                self.ration -= 1
        node.next, node.prev = self.head.next, self.head.next.prev
        self.head.next.prev = node
        self.head.next = node
    def get(self, key):
        node = self.hash[key]
        if node:
            node.prev.next, node.next.prev = node.next, node.prev
            # self.head.next, self.head.next.prev, node.next, node.prev = node, node, self.head.next, self.head
            node.next, node.prev = self.head.next, self.head.next.prev
            self.head.next.prev = node
            self.head.next = node
            return node.val
        return -1

    def put(self, key, value):
        node = self.hash[key]
        if node:
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev
        else:
            node = DLinkedList(value, key)
            self.hash[key] = node
            if not self.ration:
                last_node = self.tail.prev
                self.tail.prev = last_node.prev
                last_node.prev.next = self.tail
                self.hash[last_node.key] = None
            else:
                self.ration -= 1
        node.next, node.prev = self.head.next, self.head.next.prev
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.hash[key]
        if node:
            deleteNode(node)
            insertNode(self.head, node)
            return node.val
        return -1

    def put(self, key, value):
        node = self.hash[key]
        if node:
            deleteNode(node)
            node.val = value
        else:
            node = DLinkedList(value, key)
            if self.sz:
                self.sz -= 1
            else:
                self.hash[self.tail.prev.key] = None
                deleteNode(self.tail.prev)
            self.hash[key] = node
        insertNode(self.head, node)
