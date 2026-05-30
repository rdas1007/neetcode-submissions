class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        copy = sorted(list(set(nums)))
        count = 1
        maxVal = 1
        print(copy)
        for i in range(len(copy)-1):
            if copy[i+1] - copy[i] == 1:
                count += 1
            else:                
                maxVal = max(maxVal, count) 
                count = 1
        maxVal = max(maxVal, count) 
        return maxVal