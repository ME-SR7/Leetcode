class Solution:
    def secondHighest(self, s: str) -> int:
        s_digit=set()
        for i in s:
            if i.isdigit():
                s_digit.add(int(i))
        first=second=float("-inf")
        for num in s_digit:
            if num>first:
                second=first
                first=num
            else:
                if num>second and num!=first:
                    second=num
        return -1 if second==float("-inf") else second
        