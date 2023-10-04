class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        v = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = 0
                
                if nums[i] < nums[j]:
                    
                    s = nums[j] -nums[i]
                if v < s:
                    v = s

        if v >= 1 :
            return v
        else:
            return -1

# Input: nums = [7,1,5,4]
# Output: 4

# Input: nums = [9,4,3,2]s
# Output: -1