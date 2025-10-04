class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter=Counter(chars)
        total=0
        for word in words:
            word_counter=Counter(word)
            word_form=True
            for ch in word_counter:
                if word_counter[ch]>chars_counter[ch]:
                    word_form=False
            if word_form:
                total+=len(word)
            
        return total        
            
        