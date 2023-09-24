class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                c += nums[i] - nums[i+1] +1
                nums[i+1] += nums[i] - nums[i+1] + 1

        return c
    
