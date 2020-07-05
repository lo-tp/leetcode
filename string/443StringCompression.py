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
