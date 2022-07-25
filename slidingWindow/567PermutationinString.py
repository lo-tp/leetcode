from collections import Counter
from copy import copy


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        originalType, originalCounter = 0, {}
        for i in s1:
            if i in originalCounter:
                originalCounter[i] += 1
            else:
                originalCounter[i] = 1
                originalType += 1
        l = 0
        type, counter = originalType, copy(originalCounter)
        for i in range(0, len(s2)):
            s = s2[i]
            if s in counter:
                if counter[s] == 1:
                    type -= 1
                    if not type:
                        return True
                elif not counter[s]:
                    while s2[l] != s:
                        if not counter[s2[l]]:
                            type += 1
                        counter[s2[l]] += 1
                        l += 1
                    counter[s] += 1
                    l += 1
                counter[s] -= 1
            else:
                type, counter = originalType, copy(originalCounter)
                l = i + 1

        return False
