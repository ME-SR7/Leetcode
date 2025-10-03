class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d_num1={}
        result=[]
        for num in nums1:
            d_num1[num]=1+d_num1.get(num,0)
        for num in nums2:
            if num in d_num1 and d_num1[num]>0 :
                result.append(num)
                d_num1[num]-=1
        return result


        