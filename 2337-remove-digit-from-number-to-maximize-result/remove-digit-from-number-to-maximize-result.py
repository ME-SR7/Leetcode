class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number=""
        for i, num in enumerate(number):
            if num == digit:
                temp=number[:i]+number[i+1:]
                if temp>max_number:
                    max_number=temp


                
        return max_number
        