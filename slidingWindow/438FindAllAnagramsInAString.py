from typing import List, Optional
from copy import copy


class Solution(object):
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, originalKind, originalCounter = [], 0, {}
        for letter in p:
            if letter not in originalCounter:
                originalCounter[letter] = 0
                originalKind += 1
            originalCounter[letter] += 1
        l, kind, counter = 0, originalKind, copy(originalCounter)
        for r in range(0, len(s)):
            letter = s[r]
            if letter in counter:
                if counter[letter] == 1:
                    if kind == 1:
                        res.append(l)
                        counter[s[l]] += 1
                        l += 1
                        kind += 1
                    kind -= 1
                elif not counter[letter]:
                    while s[l] != letter:
                        if not counter[s[l]]:
                            kind += 1
                        counter[s[l]] += 1
                        l += 1
                    counter[letter] += 1
                    l += 1
                counter[letter] -= 1
            else:
                l, kind, counter = r + 1, originalKind, copy(originalCounter)
        return res
