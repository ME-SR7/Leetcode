class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count_s=Counter(s)
        count_t=Counter(target)
        return min(count_s[t]//count_t[t] for t in count_t )
        
        