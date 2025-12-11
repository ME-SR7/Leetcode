class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start=1
        end=len(arr)-2
        while start<=end:
            mid=start+(end-start)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]:
                end=mid-1
            else:
                start=mid+1
        