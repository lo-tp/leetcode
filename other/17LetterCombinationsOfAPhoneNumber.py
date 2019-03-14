class Solution(object):
    def letterCombinations(self, digits):
        if len(digits):
            s1, s2, mapping = [''], [], [0, 0, 'abc', 'def',
                                         'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
            for d in digits:
                digit = int(d)
                s2, s1, = s1, s2
                while s2:
                    k = s2.pop()
                    for letter in mapping[digit]:
                        s1.append(k+letter)
            return s1
        return []
