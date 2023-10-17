class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in range(len(nums)):
            if original in nums:
                original *= 2
        # else:
        return original





        # while original in nums:
        #     original *= 2

        # return original
       
        
# Input: nums = [2,7,9], original = 4
# Output: 4

# Input: nums = [5,3,6,1,12], original = 3
# Output: 24