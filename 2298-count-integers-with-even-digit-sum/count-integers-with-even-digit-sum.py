class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            print(i)
            sum=0
            n=i
            while n>0:
                sum+=n%10
                n//=10
            if sum%2==0:
                count+=1
            
        return count















        