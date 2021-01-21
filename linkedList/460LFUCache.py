class Node():
    def __init__(self, key, val, freq):
        self.next, self.prev, self.val, self.key, self.freq = None, None, val, key, freq


def insertAfter(prev, node):
    prev_next = prev.next
    prev.next, prev_next.prev = node, node
    node.prev, node.next = prev, prev_next


def remove(node):
    prev, next = node.prev, node.next
    prev.next, next.prev = next, prev


class LFUCache(object):

    def __init__(self, capacity):
        self.freq_list = {}
        self.key_node = {}
        self.least_freq = 1
        self.capacity = capacity
        self.work = capacity != 0

    def insert(self, node):
        freq = node.freq
        if freq not in self.freq_list:
            head, tail = Node(-1, -1, -1), Node(-1, -1, -1)
            head.next, tail.prev = tail, head
            self.freq_list[freq] = (head, tail)
        insertAfter(self.freq_list[freq][0], node)

    def get(self, key):
        if self.work:
            if key in self.key_node:
                node = self.key_node[key]
                remove(node)
                freq = node.freq
                if self.freq_list[freq][0].key == -1 and self.freq_list[freq][0].next.key == -1:
                    self.least_freq += 1
                node.freq += 1
                self.insert(node)
                return node.val
        return -1

    def put(self, key, value):
        if self.work:
            node = None
            if key in self.key_node:
                node = self.key_node[key]
                remove(node)
                freq = node.freq
                if self.freq_list[freq][0].key == -1 and self.freq_list[freq][0].next.key == -1:
                    self.least_freq += 1
                node.freq += 1
                node.val = value
            else:
                node = Node(key, value, 1)
                self.key_node[key] = node
                if not self.capacity:
                    to_remove = self.freq_list[self.least_freq][1].prev
                    remove(to_remove)
                    del self.key_node[to_remove.key]
                else:
                    self.capacity -= 1
                self.least_freq = 1
            self.insert(node)
