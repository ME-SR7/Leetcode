class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        lst = ["000","111","222","333","444","555","666","777","888","999"]
        new=[]
        for n in lst:
            if n in num:
                new.append(n)
        return max(new) if new else ""
        
               
        
