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
