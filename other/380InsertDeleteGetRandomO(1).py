from random import choice


class RandomizedSet(object):

    def __init__(self):
        self.data, self.index, self.sz = [], {}, 0

    def insert(self, val):
        if val not in self.index:
            self.data.append(val)
            self.index[val] = self.sz
            self.sz += 1
            return True
        return False

    def remove(self, val):
        if val in self.index:
            self.sz -= 1
            self.index[self.data[-1]] = self.index[val]
            self.data[self.index[val]] = self.data.pop()
            del self.index[val]
            return True
        return False

    def getRandom(self):
        return choice(self.data)
