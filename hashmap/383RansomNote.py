from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count, m_count=Counter(ransomNote), Counter(magazine)
        for k,v in r_count.items():
            if k not in m_count or m_count[k]<v:
                return False

        return True
        
