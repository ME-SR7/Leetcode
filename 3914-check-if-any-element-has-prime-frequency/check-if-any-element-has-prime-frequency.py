class Solution:
   
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        
        dict_seen={}
        for num in nums:
            dict_seen[num]=1+dict_seen.get(num,0)

        for count in dict_seen.values():
            if count<2:
                continue
            if count==2 or count==3:
                return True
            is_prime=True
            for j in range(2,int((count**0.5)+1)):
                if count%j==0:
                    is_prime=False
                    break
            if is_prime:
                return True        
                
        return False
        

         
        