class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter=Counter(ransomNote)
        m_counter=Counter(magazine)
        for key,values in r_counter.items():
            if m_counter.get(key,0)<values:
                return False
        return True