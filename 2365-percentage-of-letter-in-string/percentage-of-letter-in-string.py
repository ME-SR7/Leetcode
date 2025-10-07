class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        output=0
        for i in range (len(s)):
            if s[i] in letter:
                count+=1
        if count==0:
            return 0
        else:
            output=int((count/len(s))*100)
        return output

        
        