class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a_in = int(a, 2)
        b_in = int(b, 2)
        c_in = a_in + b_in
        return bin(c_in)[2:]