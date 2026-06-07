class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        new_Arr = sorted(nums1)
        print(new_Arr)
        l = len(new_Arr) 
        if l%2 == 0:
            median = (new_Arr[l//2] + new_Arr[(l//2) - 1]) / 2
        else:
            median = new_Arr[l//2]
        return median