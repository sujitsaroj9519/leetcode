class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)

        return l
    
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]