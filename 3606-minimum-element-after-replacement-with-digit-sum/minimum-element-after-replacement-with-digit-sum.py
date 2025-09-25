class Solution:
    def minElement(self, nums: List[int]) -> int:
        output=[]
        for num in nums:
            sum=0
            while num>0:
                sum+=num%10
                num//=10
            output.append(sum)
        return min(output)