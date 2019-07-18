from collections import defaultdict


class TreeMap():
    def __init__(self, default_val):
        self.data = default(lambda: default_val)

    def keys(self):
        return self.data.keys().sort()

    def get(self, key):
        return self.data[key]

    def set(self, key, val):
        self.data[key] = val


class MyCalendarTwoWithTreeMap(object):

    def __init__(self):
        self.tm = TreeMap(0)

    def book(self, start, end):
        tm = self.tm
        tm.set(start, tm.get(start)+1)
        tm.set(end, tm.get(end)-1)
        active = 0
        for key in tm.keys():
            active += tm.get(key)
            if active > 2:
                tm.set(start, tm.get(start)-1)
                tm.set(end, tm.get(end)+1)
                return False
        return True

class MyCalendarTwoBetter(object):

    def __init__(self):
        self.single = []
        self.double = []

    def book(self, start, end):
        for s, e in self.double:
            if s < end and e > start:
                return True
        for s, e in self.single:
            if s < end and e > start:
                self.double.append(max(start, s), min(end, e))
        self.single.append((start, end))
def convert(s, e, h, t):
    if s <= h and e > h and e < t:
        return (h, e)
    elif h <= s and t > s and t < e:
        return (s, t)
    elif s <= h and e >= t:
        return (h, t)
    elif h <= s and t >= e:
        return (s, e)
    return (-1, -1)


class MyCalendarTwo(object):

    def __init__(self):
        self.original = []
        self.double = []

    def book(self, start, end):
        for s, e in self.double:
            h, t = convert(start, end, s, e)
            if h != -1:
                return False

        for s, e in self.original:
            h, t = convert(start, end, s, e)
            if h != -1:
                self.double.append((h, t))
        self.original.append((start, end))
        return True
