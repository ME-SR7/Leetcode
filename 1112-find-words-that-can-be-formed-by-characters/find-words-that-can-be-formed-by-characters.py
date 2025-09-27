class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter=Counter(chars)
        total=0
        for word in words:
            word_counter=Counter(word)
            if all(word_counter[ch]<=chars_counter[ch] for ch in word_counter):
                total+=len(word)
            
        return total        
            
        