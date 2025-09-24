class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i
            output=num+1
        result=0
        result=[int(ch) for ch in str(output)]
        return result

        
        # num = int("".join(map(str, digits)))
        # num += 1
        # return [int(d) for d in str(num)]
        