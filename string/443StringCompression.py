class Solution(object):
    def compress(self, chars):
        chars.append('-1')
        index, count, char = -1, 2, -1
        for i in chars:
            if i != char:
                if count > 1:
                    for j in '{}'.format(count):
                        chars[index] = j
                        index += 1
                count, char = 1, i
                chars[index] = char
                index += 1
            else:
                count += 1
        return index-1
    def compress(self, chars):
        sz, index, count, char = len(chars)-1, 1, 0, chars[0]
        for i, c in enumerate(chars):
            if c == char:
                count += 1
            if i == sz or c != char:
                if count > 1:
                    for j in '{}'.format(count):
                        chars[index] = j
                        index += 1
                if c != char:
                    char = chars[index] = c
                    index += 1
                    count = 1
        return index

