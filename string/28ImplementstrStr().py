def getTable(string):
    k, sz, table = -1, len(string), [-1 for _ in string]
    for i in range(1, sz):
        while k != -1 and string[k+1] != string[i]:
            k = table[k]
        if string[k+1] == string[i]:
            k += 1
        table[i] = k
    return table


class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if haystack:
            sz, table, k = len(needle), getTable(needle), -1
            for index, i in enumerate(haystack):
                while k != -1 and needle[k+1] != haystack[i]:
                    k = table[k]
                if needle[k+1] == haystack[i]:
                    k += 1
                if k+1 == sz:
                    return index
        return -1
