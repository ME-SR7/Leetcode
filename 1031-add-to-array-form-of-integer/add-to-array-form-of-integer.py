class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num)-1
        carry=k
        while i>=0 and carry>=0:
                carry+=num[i]
                num[i]=carry%10
                carry//=10
                i-=1
        while carry:
                num.insert(0,carry%10)
                carry//=10
        return num
                 
        