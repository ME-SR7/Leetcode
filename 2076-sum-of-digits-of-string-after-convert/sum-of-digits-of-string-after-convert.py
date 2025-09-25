class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_str=""
        for i in s:
            s_str+=str(ord(i)-ord('a')+1)
        for _ in range(k):
            total=0
            for i in s_str:
                total+=int(i)
            s_str=str(total)

        return total
           


        