class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_nums=0
        max_sum=nums[0]
        for num in nums:
            sum_nums+=num
            max_sum=max(sum_nums,max_sum)
            if sum_nums<0:
                sum_nums=0
        return max_sum
        